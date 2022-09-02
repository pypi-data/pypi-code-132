import numpy as np
import pandas as pd
from Bio import SeqIO
from quasinet.qnet import Qnet, qdistance, save_qnet, load_qnet


class Enet(object):
    """Emergenet architecture.

    Parameters
    ----------
    seq : str
        The target sequence to be analysed by Emergenet
        Either nucleotide/amino-acid sequence or fasta file path (containing '.fasta')

    seq_trunc_length : int
        Length to truncate sequences in Qnet analysis
        Sequences used to train Qnet and compute q-distance must be of same length

    seq_metadata : str
        Describes the sequence; added automatically if 'seq' is a fasta file path

    random_state : int
        Sets seed for random number generator
    """

    def __init__(self, seq, seq_trunc_length, seq_metadata=None, random_state=None):
        if seq.endswith('.fasta'):
            if self._count_seqs(seq) != 1:
                raise ValueError('The file must contain exactly 1 sequence!')
            for record in SeqIO.parse(seq, 'fasta'):
                self.seq = str(record.seq.upper())
                self.seq_metadata = str(record.description)
        else:
            self.seq = seq.upper()
            self.seq_metadata = seq_metadata

        if seq_trunc_length > len(self.seq):
            raise ValueError('Length to truncate sequences must not be greater than target sequence length!')
        self.seq_trunc_length = seq_trunc_length

        if random_state < 0:
            raise ValueError('Seed must be between 0 and 2**32 - 1!')
        self.random_state = random_state

    def __repr__(self):
        return "emergenet.Emergenet"

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def _count_seqs(filepath):
        """Returns number of sequences in a fasta file.

        Parameters
        ----------
        filepath : str
            File name

        Returns
        -------
        seq_df : int
            Number of sequences
        """
        with open(filepath, 'r') as f:
            fasta = SeqIO.parse(f, 'fasta')
            if not any(fasta):
                raise ValueError('The infile must be in fasta format!')
        with open(filepath, 'r') as f:
            lines = f.read()
        num_sequences = lines.count('>')
        return num_sequences

    def _parse_fasta(self, filepath):
        """Parses a fasta file and returns DataFrame with two columns.
        `id` contains fasta metadata.
        `sequence` contains sequences truncated to `seq_trunc_length` as character array.

        Parameters
        ----------
        filepath : str
            File name

        Returns
        -------
        seq_df : pd.DataFrame
            DataFrame of sequences
        """
        if self._count_seqs(filepath) < 1:
            raise ValueError('The file contains no sequences!')
        ids = []
        seqs = []
        for record in SeqIO.parse(filepath, 'fasta'):
            if len(record.seq) < self.seq_trunc_length:
                continue
            ids.append(str(record.id))
            seqs.append(np.array(record.seq[:self.seq_trunc_length].upper()))
        seq_df = pd.DataFrame({'id': ids, 'sequence': seqs})
        return seq_df

    def _sequence_array(self, seq_df, sample_size=None):
        """Extracts array of sequence arrays from DataFrame; includes target sequence.

        Parameters
        ----------
        seq_df : pd.DataFrame
            DataFrame containing sequences

        sample_size : int
            Number of strains to sample

        Returns
        -------
        seq_lst: numpy.ndarray
            Array of sequence arrays
        """
        if 'sequence' not in seq_df.columns:
            return ValueError('The DataFrame must store sequences in `sequence` column!')
        if sample_size is None or sample_size > len(seq_df):
            sample_size = len(seq_df)
        seqs = seq_df['sequence'].sample(sample_size, random_state=self.random_state).values
        seq_lst = []
        for seq in seqs:
            seq_lst.append(seq)
        seq_lst.append(np.array(list(self.seq[:self.seq_trunc_length])))
        seq_lst = np.array(seq_lst)
        return seq_lst

    def load_data(self, filepath, outfile=None):
        """Loads fasta file data and optionally saves to CSV.

        Parameters
        ----------
        filepath : str
            File name

        outfile : str
            File name to save to ('.csv')

        Returns
        -------
        seq_df : pd.DataFrame
            DataFrame of sequences
        """
        seq_df = self._parse_fasta(filepath)
        if outfile is not None:
            if not outfile.endswith('.csv'):
                raise ValueError('The outfile must end with `.csv`!')
            seq_df.to_csv(outfile, index=False)
        return seq_df

    def train(self, seq_df, sample_size=None, n_jobs=1):
        """Trains a Qnet model.

        Parameters
        ----------
        seq_df : pd.DataFrame
            DataFrame of sequences

        sample_size : int
            Number of strains to train Qnet on

        n_jobs : int
            Number of CPUs to use when training

        Returns
        -------
        qnet : Qnet
            Trained Qnet
        """
        if len(seq_df) < 1:
            raise ValueError('The DataFrame contains no sequences!')
        seq_arr = self._sequence_array(seq_df, sample_size)
        qnet = Qnet(feature_names=['x' + str(i) for i in np.arange(self.seq_trunc_length)],
                    random_state=self.random_state, n_jobs=n_jobs)
        qnet.fit(seq_arr)
        return qnet

    def emergence_risk(self, seq_df, qnet, sample_size=None):
        """Computes emergence risk score.

        Parameters
        ----------
        seq_df : pd.DataFrame
            DataFrame of sequences

        qnet : Qnet
            Qnet that sequences in seq_df belong to

        sample_size : int
            Number of strains to compute emergence risk with

        Returns
        -------
        emergence_risk_score : int
            Emergence risk score
        """
        if len(seq_df) < 1:
            raise ValueError('The DataFrame contains no sequences!')
        seq_arr = self._sequence_array(seq_df, sample_size)
        qdist_sum = 0
        target_seq = np.array(list(self.seq[:self.seq_trunc_length]))
        for i in range(len(seq_arr)):
            qdist_sum += qdistance(target_seq, seq_arr[i], qnet, qnet)
        emergence_risk_score = qdist_sum / len(seq_arr)
        return emergence_risk_score


def save_model(qnet, outfile, low_mem=False):
    """Saves a Qnet model.

    Parameters
    ----------
    qnet : Qnet
        A Qnet instance

    outfile : str
        File name to save to ('.joblib')

    low_mem : bool
        If True, save the Qnet with low memory by deleting all data attributes except the tree structure

    Returns
    -------
    None
    """
    save_qnet(qnet, outfile, low_mem)


def load_model(filepath):
    """Loads a Qnet model.

    Parameters
    ----------
    filepath : str
        File name

    Returns
    -------
    qnet : Qnet
        A Qnet instance
    """
    qnet = load_qnet(filepath)
    return qnet
