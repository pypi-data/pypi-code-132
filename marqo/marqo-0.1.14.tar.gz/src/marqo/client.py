import base64
from typing import Any, Dict, List, Optional, Union
from marqo.index import Index
from marqo.config import Config
from marqo._httprequests import HttpRequests
from marqo import utils, enums
from marqo import errors

class Client:
    """
    A client for the marqo API

    A client instance is needed for every marqo API method to know the location of
    marqo and its permissions.
    """
    def __init__(
        self, url: str = "http://localhost:8882", main_user: str = None, main_password: str = None,
        indexing_device: Optional[Union[enums.Devices, str]] = None,
        search_device: Optional[Union[enums.Devices, str]] = None
    ) -> None:
        """
        Parameters
        ----------
        url:
            The url to the S2Search API (ex: http://localhost:8882)
        """
        self.main_user = main_user
        self.main_password = main_password
        if (main_user is not None) and (main_password is not None):
            self.url = utils.construct_authorized_url(url_base=url, username=main_user, password=main_password)
        else:
            self.url = url
        self.config = Config(self.url, indexing_device=indexing_device, search_device=search_device)
        self.http = HttpRequests(self.config)

    def create_index(
        self, index_name: str,
        treat_urls_and_pointers_as_images=False, model=None,
        normalize_embeddings=True,
        sentences_per_chunk=2,
        sentence_overlap=0,
        image_preprocessing_method=None,
    ) -> Dict[str, Any]:
        """

        Args:
            index_name:
            treat_urls_and_pointers_as_images:
            model:
            normalize_embeddings:
            sentences_per_chunk:
            sentence_overlap:
            image_preprocessing_method:

        Returns:

        """
        return Index.create(
            config=self.config, index_name=index_name,
            treat_urls_and_pointers_as_images=treat_urls_and_pointers_as_images,
            model=model, normalize_embeddings=normalize_embeddings,
            sentences_per_chunk=sentences_per_chunk, sentence_overlap=sentence_overlap,
            image_preprocessing_method=image_preprocessing_method
        )

    def delete_index(self, index_name: str) -> Dict[str, Any]:
        """Deletes an index

        Args:
            index_name: name of the index

        Returns:
            response body about the result of the delete request
        """
        try:
            res = self.http.delete(path=f"indexes/{index_name}")
        except errors.MarqoWebError as e:
            return e.message

    def get_index(self, index_name: str) -> Index:
        """Get the index.
        This index should already exist.

        Parameters
        ----------
        index_name:
            UID of the index.

        Returns
        -------
        index:
            An Index instance containing the information of the fetched index.

        Raises
        ------
        s2SearchApiError
            An error containing details about why marqo can't process your request. marqo error codes are described here: https://docs.marqo.com/errors/#marqo-errors
        """
        ix = Index(self.config, index_name)
        # verify it exists
        # maybe delete - use stats end point for now
        self.http.get(path=f"indexes/{index_name}/stats")
        return ix

    def index(self, index_name: str) -> Index:
        """Create a local reference to an index identified by UID, without doing an HTTP call.
        Calling this method doesn't create an index in the marqo instance, but grants access to all the other methods in the Index class.

        Parameters
        ----------
        index_name:
            UID of the index.

        Returns
        -------
        index:
            An Index instance.
        """
        if index_name is not None:
            return Index(self.config, index_name=index_name)
        raise Exception('The index UID should not be None')

    def get_version(self) -> Dict[str, str]:
        """Get version marqo

        Returns
        -------
        version:
            Information about the version of marqo.

        Raises
        ------
        s2SearchApiError
            An error containing details about why marqo can't process your request. marqo error codes are described here: https://docs.marqo.com/errors/#marqo-errors
        """
        return self.http.get(self.config.paths.version)

    def version(self) -> Dict[str, str]:
        """Alias for get_version

        Returns
        -------
        version:
            Information about the version of marqo.

        Raises
        ------
        s2SearchApiError
            An error containing details about why marqo can't process your request. marqo error codes are described here: https://docs.marqo.com/errors/#marqo-errors
        """
        return self.get_version()

    @staticmethod
    def _base64url_encode(
        data: bytes
    ) -> str:
        return base64.urlsafe_b64encode(data).decode('utf-8').replace('=','')
