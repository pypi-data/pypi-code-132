import json

from cryptotoolbox.connector import crypto_connector

from scipy import stats
import pandas as pd
from numpy.lib.stride_tricks import as_strided as stride
from cryptotoolbox.realtime import realtime_plotting_utility
from cryptotoolbox.risk_metrics import riskmetrics
from cryptotoolbox.analyzer import market

import plotly.express as px
from itertools import cycle

palette = cycle(px.colors.qualitative.Plotly)

import numpy as np

def strat_daily_ETH(y, eth='ETH', long_expo = 1., short_expo = 0., rebalancing_day=5):  # On rentre le dataframe
    weekday = y.weekday.values
    cours = y[eth].values
    T = np.size(weekday)
    S = np.zeros(T)
    for t in range(30, T):
        if weekday[t] == rebalancing_day and cours[t - 22] > 0:
            if cours[t] > cours[t - 14] * 1.05 or cours[t] > cours[t - 21] * 1.1:
                S[t] = long_expo
            else:
                S[t] = short_expo
        else:
            S[t] = S[t - 1]
    return S


#def strat_daily_BTC(y, btc='BTC', p1=1.1, p2=1.2, long_expo = 1., short_expo = 0.):  # On rentre le dataframe
def strat_daily_BTC(y, btc='BTC', p1=1.05, p2=1.1, long_expo=1., short_expo=0., rebalancing_day=5):  # On rentre le dataframe
    weekday = y.weekday.values
    cours = y[btc].values
    T = np.size(weekday)
    S = np.zeros(T)
    for t in range(22, T):
        if weekday[t] == rebalancing_day and cours[t - 22] > 0:
            if cours[t] > cours[t - 14] * p1 and cours[t] > cours[t - 21] * p2:
                S[t] = long_expo
            else:
                S[t] = short_expo
        else:
            S[t] = S[t - 1]
    return S

def roll(df, w):
    v = df.values
    d0, d1 = v.shape
    s0, s1 = v.strides
    restricted_length = d0 - (w - 1)
    a = stride(v, (restricted_length, w, d1), (s0, s0, s1))
    rolled_df = pd.concat({
        row: pd.DataFrame(values, columns=df.columns)
        for row, values in zip(df.index[-restricted_length:], a)
    })
    return rolled_df.groupby(level=0)

def compute_alpha_signal_lo(df=None, core_tokens=['BTC', 'ETH'], extra_tokens=['AVAX'], rebalancing_day=6,lo_sig_suffix='LO',compute_lo_strat=True, plot_html=False):
    all_tokens = core_tokens + extra_tokens
    df['weekday'] = df.index.weekday
    df['rebalance'] = df.index.weekday == rebalancing_day
    for me_token in all_tokens:
        df[f'return_{me_token}'] = df[f'close_{me_token}'].pct_change().fillna(0)
    df.replace([np.inf], 0, inplace=True)
    weekly = pd.DataFrame(index=df.index,
                          data={'SBTC': strat_daily_BTC(df, 'close_BTC', 1, 1, rebalancing_day=rebalancing_day)})
    addw = pd.DataFrame(index=df.index,
                        data={'S{}'.format('ETH'): strat_daily_ETH(df, 'close_ETH', rebalancing_day=rebalancing_day)})
    weekly = weekly.join(addw, how='left')
    for i in extra_tokens:
        addw = pd.DataFrame(index=df.index, data={'S{}'.format(i): strat_daily_BTC(df, f'close_{i}')})
        weekly = weekly.join(addw, how='left')
    dfsig = weekly.copy()
    dfsig2 = dfsig.copy()
    ######
    df = pd.merge(df.copy(), dfsig2.copy(), how='left', right_index=True, left_index=True)
    signal_df = df.copy()
    signal_df = signal_df.fillna(0.)
    signal_df['Counter'] = 0
    for i in all_tokens:
        if 'S{}'.format(i) in signal_df.columns:
            signal_df['Counter'] += signal_df['S{}'.format(i)]

    def expo(y, n_max=3):
        S = np.zeros(np.size(y))
        for i in range(np.size(y)):
            if y[i] > n_max:
                S[i] = 1 / y[i]
            elif y[i] > 0:
                S[i] = 1. / n_max
            else:
                S[i] = 0
        return S

    n_max = int(len(all_tokens) / 2.) + 1
    signal_df['expo'] = expo(signal_df['Counter'].values, n_max=n_max)

    for me_tok in all_tokens:
        if not 'S{}'.format(me_tok) in signal_df.columns:
            signal_df[f'S{me_tok}'] = 0.

    for me_tok in all_tokens:
        signal_df[f'SE{me_tok}'] = signal_df[f'S{me_tok}'] * signal_df['expo']

    for i in all_tokens:
        signal_df[f'S{lo_sig_suffix}{i}'] = signal_df[f'SE{i}'].shift(1)

    signal_df[f'total_expo'] = 0.
    for me_tok in all_tokens:
        signal_df[f'total_expo'] = signal_df[f'total_expo'] + signal_df[f'S{lo_sig_suffix}{me_tok}']

    fin_df = signal_df.copy()
    if compute_lo_strat:
        def compute_return(row, tokens=[]):
            total_return = 0.
            for me_tok in tokens:
                total_return = total_return + row[f'return_{me_tok}'] * row[f'S{lo_sig_suffix}{me_tok}']
            return total_return

        comp_ret = lambda x: compute_return(x, tokens=all_tokens)
        fin_df['TR'] = fin_df.apply(comp_ret, axis=1)
        fin_df['TR'] = fin_df['TR'].fillna(0.)
        me_strat = 'strat'
        fin_df[me_strat] = np.cumprod(1 + fin_df['TR'].values)
        if plot_html:
            dollar_df = fin_df[['strat']].copy()
            new_names = {'strat': 'Absolute Return Weekly LO Strategy'}
            dollar_df = dollar_df.rename(columns=new_names)
            fig = realtime_plotting_utility.plot_dollar_multiple_time_series(data_df=dollar_df,
                                                                             logy=True, split=False,
                                                                             put_on_same_scale=False,
                                                                             title=f'strategy performance')
            fig.show()

    return fin_df.copy()

def aggregate_alpha_signal(daily_crypto_starting_date=None, daily_crypto_ending_date = None, ssj_against = 'USDT', core_tokens = ['BTC','ETH'], extra_tokens = ['AVAX'] , frequence = 'Frequency.DAILY', local_root_directory=None, refetch_pricing=True):
    aggregated_df = None
    hourly_prices = (frequence == 'Frequency.HOURLY')
    for me_symb in core_tokens + extra_tokens:
        print(f'requesting {me_symb}')
        data_df = None
        try:
            if hourly_prices:
                data_df = crypto_connector.fetch_crypto_hourly_data(ssj=me_symb,
                                                                    ssj_against=ssj_against,
                                                                    local_root_directory=local_root_directory,
                                                                    hourly_return_pkl_filename_suffix='hourly_coin_investigation.pkl',
                                                                    refetch_all=refetch_pricing,
                                                                    daily_crypto_starting_day=daily_crypto_starting_date,
                                                                    daily_crypto_ending_day=daily_crypto_ending_date)
            else:
                data_df = crypto_connector.fetch_crypto_daily_data(ssj=me_symb,
                                                                   ssj_against=ssj_against,
                                                                   local_root_directory=local_root_directory,
                                                                   daily_return_pkl_filename_suffix='daily_coin_investigation.pkl',
                                                                   refetch_all=refetch_pricing,
                                                                   daily_crypto_starting_day=daily_crypto_starting_date,
                                                                   daily_crypto_ending_day=daily_crypto_ending_date,
                                                                   saving=True)
        except Exception as e:
            print(f'trouble {e}')

        data_df = data_df.rename(columns={'close': f'close_{me_symb}'})
        data_df = data_df.rename(columns={'open': f'open_{me_symb}'})
        data_df = data_df.rename(columns={'high': f'high_{me_symb}'})
        data_df = data_df.rename(columns={'low': f'low_{me_symb}'})
        data_df = data_df.rename(columns={'volumeto': f'volume_{me_symb}'})
        data_df = data_df.rename(columns={'volume': f'volume_{me_symb}'})

        data_df = data_df.replace(0, np.nan)
        data_df = data_df[
            [f'close_{me_symb}', f'open_{me_symb}', f'high_{me_symb}', f'low_{me_symb}', f'volume_{me_symb}']]
        if aggregated_df is None:
            aggregated_df = data_df.copy()
        else:
            aggregated_df = pd.merge(aggregated_df.copy(), data_df.copy(), left_index=True, right_index=True)

    return aggregated_df

def compute_alpha_signal_ls(lo_df=None, core_tokens=['BTC', 'ETH'], extra_tokens=['AVAX'], moderating_factor = 0.1, lookback_window =90, pente_window = 30, me_center = 0.5, mix_lo = True, me_short = True,ls_signal_suffix = 'LS',aggregate_and_save = True,plot_subsignal_html = True,extract_subsignal_kpi = True):
    import numpy as np
    import functools
    from cryptotoolbox.signal import signal_utility
    from cryptotoolbox.realtime import realtime_plotting_utility
    from cryptotoolbox.risk_metrics import riskmetrics
    ssjs =  core_tokens + extra_tokens
    univ = '_'.join(ssjs)
    aggregated_signals_df = None
    for ssj in ssjs:
        current = f'univ{univ}_lookback_{lookback_window}_pente_{pente_window}_short_{me_short}_center_{me_center}.plkl'
        print('#########'+current)

        data_df = lo_df.copy()
        print('computing weekly signals')

        weekly_df = data_df.copy()
        weekly_df = weekly_df[weekly_df['rebalance']]

        def compute_ranked_slope(short, center, lagging_df):
            lagging_df['rolling_slope_rank'] = lagging_df['rolling_slope'].rank(pct=True)
            if short :
                lagging_df['rolling_slope_rank_ls'] = 2 * lagging_df['rolling_slope_rank'] - center
                lagging_df['rolling_slope_rank_ls'] = lagging_df['rolling_slope_rank_ls'].clip(-1,1)
            else:
                lagging_df['rolling_slope_rank_ls'] = lagging_df['rolling_slope_rank']

            gen_sig = lagging_df['rolling_slope_rank_ls'].iloc[-1]
            return gen_sig

        def compute_slope(slope_df):
           y = slope_df.values
           slope = stats.linregress(np.arange(len(y)), y).slope
           return slope

        weekly_df['rolling_slope'] = weekly_df[f'close_{ssj}'].rolling(window=pente_window).apply(compute_slope)


        go = functools.partial(compute_ranked_slope,me_short,me_center)
        signal_df = roll(weekly_df, lookback_window).apply(go)

        signal_df = signal_df.to_frame()
        signal_df.columns = ['signal_gen']

        data_df = pd.merge(data_df.copy(), signal_df.copy(),how='left', right_index=True, left_index=True)
        data_df['signal_gen']=data_df['signal_gen'].ffill()

        data_df['signal'] = data_df['signal_gen'].shift()
        if aggregate_and_save:
            sig_to_save = data_df[[f'close_{ssj}','signal']].copy()
            if aggregated_signals_df is None:
                sig_to_save.columns = [f'close_{ssj}',f'S{ls_signal_suffix}{ssj}']
                aggregated_signals_df = sig_to_save.copy()
            else :
                sig_to_save.columns = [f'close_{ssj}',f'S{ls_signal_suffix}{ssj}']
                aggregated_signals_df = pd.merge(aggregated_signals_df.copy(), sig_to_save.copy(), left_index = True, right_index=True)


        data_df = data_df.dropna()
        data_df['epoch_number'] = data_df['rebalance'].cumsum()

        perf_df = data_df.copy()
        perf_df=perf_df.rename(columns={f'close_{ssj}':'close'})
        freqly_df, _ = signal_utility.reconstitute_signal_perf(data=perf_df, transaction_cost=True,
                                                               normalization=False)

        if plot_subsignal_html:
            fig = realtime_plotting_utility.plot_multiple_time_series(freqly_df[['signal']],logy = False,drop_na_inf = False, title = ssj)
            fig.show()
            fig = realtime_plotting_utility.plot_multiple_time_series(freqly_df[['reconstituted_perf', 'reconstituted_under']],put_on_same_scale = False, drop_na_inf = False, title = ssj)
            fig.show()
            fig1 = realtime_plotting_utility.plot_multiple_time_series(freqly_df[['reconstituted_perf', 'reconstituted_under']],logy = False, put_on_same_scale = False, drop_na_inf = False, title = ssj)
            fig1.show()


        if extract_subsignal_kpi:
            def compute_metrics(df, strat=None):
                kpi_df = riskmetrics.get_kpi(df[[strat]])
                return kpi_df.to_dict()[strat]

            me_strat = 'reconstituted_perf'
            go_comp_kpi = lambda x: compute_metrics(x, strat=me_strat)

            epochkpis_df = freqly_df[['epoch_number', me_strat]].groupby(['epoch_number']).apply(go_comp_kpi)
            epochkpis_df = epochkpis_df.sort_index()
            epochkpis_df = pd.DataFrame.from_records(epochkpis_df.to_dict()).T



            strat_data_df = freqly_df[['reconstituted_perf', 'reconstituted_under']].copy()
            #strat_data_df = strat_data_df[strat_data_df.index >= '2021-02-01'].copy()
            ma = market.MarketAnalyzer(strat_data_df, hourlyze = True)

            print(f'computing kpis for underlying {ssj}')
            kpi_df = ma.get_kpi().T
            kpi_df=kpi_df.dropna()
            kpi_df=kpi_df[~np.isnan(kpi_df.sharpe)]
            kpi_df = kpi_df[kpi_df.index == 'reconstituted_perf']
            print(kpi_df.head())

    def curate_signals(row,under='BTC'):
        if abs(row[f'close_{under}']) <= 1e-3:
            return np.nan
        else:
            return row[f'S{ls_signal_suffix}{ssj}']

    for ssj in ssjs:
        go_curate = lambda x: curate_signals(x, under=ssj)
        aggregated_signals_df[f'S{ls_signal_suffix}{ssj}'] = aggregated_signals_df.apply(go_curate, axis=1)

    aggregated_signals_df = aggregated_signals_df.dropna()
#    aggregated_signals_df = aggregated_signals_df[~aggregated_signals_df[f'S{ls_signal_suffix}BTC'].isna().values]
#    aggregated_signals_df = aggregated_signals_df.fillna(0.)

    if mix_lo:
        aggregated_signals_df = pd.merge(aggregated_signals_df.copy(), lo_df.copy(),suffixes=['','_lo'], how='left',
                                         left_index=True, right_index=True)
        def compute_mix_signals(row_df, core_tokens= None, extra_tokens= None):
            lo_expo = row_df['expo']
            if lo_expo > 0 :
                return {f'SF{tok}':row_df[f'SLO{tok}'] for tok in core_tokens + extra_tokens}
            else :
                return {f'SF{tok}':row_df[f'SLS{tok}'] for tok in core_tokens + extra_tokens}

        go_mix = lambda x : compute_mix_signals(x, core_tokens=core_tokens, extra_tokens=extra_tokens)
        nex_signals_series = aggregated_signals_df.apply(go_mix, axis=1)
        nex_signals_df = pd.DataFrame().from_records(nex_signals_series.values)
        nex_signals_df.index = nex_signals_series.index
        aggregated_signals_df = pd.merge(nex_signals_df.copy(),aggregated_signals_df.copy(),left_index=True, right_index=True)
    else :
        for tok in core_tokens + extra_tokens:
            aggregated_signals_df[f'SF{tok}']=aggregated_signals_df[f'SLS{tok}']

    def compute_ls_expo(row_df, universe = None, moderating_factor = np.nan):
        bullish_ones = []
        bearish_ones = []
        bullish_dic = {}
        bearish_dic = {}
        bullish_magnitude = 0.
        bearish_magnitude = 0.
        compo = {}
        for sig in [f'SF{me_tok}' for me_tok in universe]:
            if row_df[sig] > 0. :
                bullish_ones.append(sig)
                bullish_dic[sig] = row_df[sig]
                bullish_magnitude = bullish_magnitude +row_df[sig]
            if row_df[sig]<0.:
                bearish_ones.append(sig)
                bearish_dic[sig] = row_df[sig]
                bearish_magnitude = bearish_magnitude +row_df[sig]

        for sig in [f'SF{me_tok}' for me_tok in universe]:
            if row_df[sig] > 0. and bullish_magnitude>moderating_factor :
                compo[sig] = row_df[sig]/bullish_magnitude*moderating_factor
                continue
            if row_df[sig] > 0.:
                compo[sig] = row_df[sig]
                continue
            if row_df[sig] < 0. and abs(bearish_magnitude)>moderating_factor:
                compo[sig] = row_df[sig]/abs(bearish_magnitude)*moderating_factor
                continue
            if row_df[sig] < 0.:
                compo[sig] = row_df[sig]
                continue
            compo[sig] = 0.

        final_long_expo = 0.
        final_short_expo = 0.
        for sig in [f'SF{me_tok}' for me_tok in universe]:
            if compo[sig]>0.:
                final_long_expo = final_long_expo + compo[sig]
            if compo[sig]<0.:
                final_short_expo = final_short_expo + compo[sig]

        compo['long_expo']  = final_long_expo
        compo['short_expo'] = final_short_expo
        compo['SCASH'] = 1.-compo['long_expo']+ compo['short_expo']
        return compo

    comp_compo = lambda x : compute_ls_expo(x, universe=ssjs, moderating_factor=moderating_factor)
    aggregated_signals_df['compo'] = aggregated_signals_df.apply(comp_compo, axis = 1)

    normed_sig_df = pd.DataFrame().from_records(aggregated_signals_df['compo'].values)
    normed_sig_df.index = aggregated_signals_df.index

    for me_tok in ssjs:
        aggregated_signals_df['return_{}'.format(me_tok)] = aggregated_signals_df['close_{}'.format(me_tok)].pct_change()
    columns_to_keep = [f'return_{me_tok}' for me_tok in ssjs] + [f'close_{me_tok}' for me_tok in ssjs]
    merged_df =  pd.merge(aggregated_signals_df[columns_to_keep].copy(), normed_sig_df.copy(), left_index = True, right_index = True)
    merged_df = merged_df.iloc[1:]
    merged_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    merged_df = merged_df.fillna(0.)

    print('computing exposition')
    def compute_strat_ret(row_df, universe = None, stable_annulalized_apy=0.03):
        aggregated_return = 0.
        for me_token in universe:
            aggregated_return = aggregated_return + row_df[f'return_{me_token}'] * row_df[f'SF{me_token}']
        daily_rate = (1+stable_annulalized_apy)**(1./365.)-1
        aggregated_return = aggregated_return + row_df[f'SCASH']*daily_rate
        return aggregated_return

    comp_ret = lambda x : compute_strat_ret(x, universe=ssjs)
    merged_df['STRAT_RETURN'] = merged_df.apply(comp_ret, axis=1)

    merged_df['COMBO_STRAT'] = np.cumprod(1 + merged_df['STRAT_RETURN'].values)
    merged_df['DOLLAR_COMBO_STRAT'] = 10000. * np.cumprod(1 + merged_df['STRAT_RETURN'].values)
    return merged_df.copy()

def compute_alpha_metrics(data_df = None, core_tokens=['BTC', 'ETH'], extra_tokens=['AVAX'], moderating_factor = 0.1, frequency='weekly', generate_kpis = True, plot_html=True, stop_loss_quantile = 0.75,take_profit_quantile = 0.75,write_excel_file = True, local_root_directory = None, plot_metrics = True,plot_html_save = True):
    ssjs = core_tokens + extra_tokens
    universe_literal = '_'.join(ssjs)
    if plot_html:
        title = f'HedgeFarm Strategy Universe {universe_literal} moderating factor {moderating_factor}'
        backtest_df = data_df[['COMBO_STRAT']].copy()
        backtest_df.columns = ['strategy']
        fig = realtime_plotting_utility.plot_multiple_time_series(
            data_df=backtest_df,
            logy=True, split=False,
            put_on_same_scale=False,
            title=title)
        fig.show()
    # KPI writing


    if generate_kpis:
        riskmetrics.compute_plot_excel_kpis_meterics_metrics(backtest_df, title,
                                                             local_root_directory, plot_html=True,
                                                             write_file=True)
        btd_kpis, ytd_kpis, past_returns = riskmetrics.compute_extensive_kpis(
            data_df=data_df.copy(), strat='COMBO_STRAT')

        go_comp_kpi = lambda x: compute_metrics(x, strat=me_strat)


        def compute_allocation(row_df, universe=None):
            compo = {}
            for me_token in universe:
                compo[me_token] = row_df[f'SF{me_token}']
            return compo


        comp_alloc = lambda x: compute_allocation(x, universe=ssjs)
        data_df['COMBO_STRAT_compo'] = data_df.apply(comp_alloc, axis=1)

        ############# strategy drawdown
        dd_data_df = data_df.copy() #pd.merge(merged_df.copy(), sol_ohlc_df.copy(), left_index=True,
                              #right_index=True)
        limited_dd_data_df = dd_data_df[dd_data_df.index >= '2021-04-01'].copy()
        limited_dd_data_df = limited_dd_data_df[limited_dd_data_df.index <= '2021-07-01'].copy()

        dd_list = []
        for me_underlying in [f'close_{ssj}' for ssj in ['BTC', 'AVAX']] + ['COMBO_STRAT']:
            dd_display_name = 'drawdown ' + me_underlying.replace('close_', '')
            dd_list.append(dd_display_name)
            ### whole period drawdown
            dd_norm_strat = riskmetrics.drawdown(dd_data_df[me_underlying])
            # merged_df[f'drawdown_{me_underlying}'] = dd_norm_strat

            dd_data_df[dd_display_name] = - dd_norm_strat
            ### limited_period_drawdown
            limited_dd_norm_strat = riskmetrics.drawdown(limited_dd_data_df[me_underlying])
            # merged_df[f'drawdown_{me_underlying}'] = dd_norm_strat
            dd_display_name = 'drawdown ' + me_underlying.replace('close_', '')
            limited_dd_data_df[dd_display_name] = - limited_dd_norm_strat



        if plot_html_save:
            new_names = {'drawdown BTC': 'Bitcoin', 'drawdown AVAX': 'AVAX',
                         'drawdown COMBO_STRAT': 'Absolute Return DeFi Strategy'}
            dd_data_df = dd_data_df.rename(columns=new_names)
            fig = realtime_plotting_utility.plot_multiple_drawdowns(dd_data_df,
                                                                    list(new_names.values()))
            fig.show()
            new_names = {'drawdown BTC': 'Bitcoin', 'drawdown AVAX': 'AVAX',
                         'drawdown COMBO_STRAT': 'Absolute Return DeFi Strategy'}
            limited_dd_data_df = limited_dd_data_df.rename(columns=new_names)
            fig = realtime_plotting_utility.plot_multiple_drawdowns(limited_dd_data_df,
                                                                    list(new_names.values()))
            fig.show()

            dollar_df = data_df[['DOLLAR_COMBO_STRAT']].copy()
            new_names = {'DOLLAR_COMBO_STRAT': 'Absolute Return DeFi Strategy'}
            dollar_df = dollar_df.rename(columns=new_names)
            fig = realtime_plotting_utility.plot_dollar_multiple_time_series(data_df=dollar_df,
                                                                             logy=True, split=False,
                                                                             put_on_same_scale=False,
                                                                             title=f'performance (exposition moderating factor {moderating_factor}  rebalancing {frequency})')
            fig.show()

            fig = realtime_plotting_utility.plot_multiple_time_series(
                data_df=data_df[['long_expo', 'short_expo']],
                logy=False, split=False,
                put_on_same_scale=False,
                title=f'long/short exposition (exposition moderating factor {moderating_factor}  rebalancing {frequency})')
            fig.show()

        print('computing KPIs per epoch')

        me_strat = 'COMBO_STRAT'
        whole_period_kpi_df = riskmetrics.get_kpi(data_df[[me_strat]])
        whole_period_kpi_df = whole_period_kpi_df.iloc[1:]

        kpi_df = riskmetrics.get_kpi(data_df[[me_strat]])
        stub = f'mf_{moderating_factor}_strat_{me_strat}'
        kpi_df.columns = [stub]
        to_store_df = data_df.copy()
        to_store_df['Date'] = to_store_df.index

        #### new fresh weights on monday
        to_store_df['has_just_rebalanced'] = to_store_df.index.weekday == 0

        to_store_df['epoch_number'] = to_store_df['has_just_rebalanced'].cumsum()
        epoch_df = to_store_df[to_store_df['has_just_rebalanced']].copy()
        epoch_df = epoch_df[
            ['epoch_number', me_strat, 'long_expo', 'short_expo', f'{me_strat}_compo']]


        def compute_metrics(df, strat=None):
            kpi_df = riskmetrics.get_kpi(df[[strat]])
            return kpi_df.to_dict()[strat]


        go_comp_kpi = lambda x: compute_metrics(x, strat=me_strat)

        epochkpis_df = to_store_df[['epoch_number', me_strat]].groupby(['epoch_number']).apply(
            go_comp_kpi)
        epochkpis_df = epochkpis_df.sort_index()
        epochkpis_df = pd.DataFrame.from_records(epochkpis_df.to_dict()).T
        final_df = pd.merge(epoch_df.copy(), epochkpis_df.copy(), left_on='epoch_number',
                            right_index=True)
        final_df = final_df.drop(columns=[me_strat])
        final_df = final_df.rename(columns={f'{me_strat}_compo': 'COMPO'})

        final_df['STRAT'] = me_strat
        final_df['STRATPARAMS'] = f'{me_strat}_{moderating_factor}'
        # final_df['frequency'] = frequency
        # final_df['moderation'] = moderating_factor
        # if moderating_factor >0.5:
        #     final_df['subscription_asset'] = me_strat.replace('STRAT','').replace('_','')
        # else:
        #     final_df['subscription_asset'] = 'USDC'
        final_df['subscription_asset'] = 'USDC'
        final_df['date'] = final_df.index

        freq_aggregated_df = final_df.copy()
        freq_aggregated_df = freq_aggregated_df.sort_values(by='epoch_number')
        # freq_aggregated_df.index = freq_aggregated_df.index.tz_localize(None)

        av_dd_df = freq_aggregated_df.groupby(['STRATPARAMS'])['mdd'].quantile(q=stop_loss_quantile)
        qt_gain_df = freq_aggregated_df.groupby(['STRATPARAMS'])['simple_return'].quantile(
            q=take_profit_quantile)

        av_dd_df = av_dd_df.to_frame()
        qt_gain_df = qt_gain_df.to_frame()

        av_dd_df.columns = ['stop loss']
        qt_gain_df.columns = ['take profit']
        av_dd_df = av_dd_df.round(decimals=2)
        qt_gain_df = qt_gain_df.round(decimals=2)

        from sklearn.preprocessing import KBinsDiscretizer


        def categorize(data_df=None, column_to_categorize=None):
            est = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
            est.fit(abs(data_df[column_to_categorize].values.reshape(-1, 1)))
            binarized_data = est.transform(abs(data_df[column_to_categorize].values.reshape(-1, 1)))
            data_df[column_to_categorize + '_rank'] = binarized_data
            return data_df.copy()


        av_dd_df_categorized = categorize(data_df=av_dd_df, column_to_categorize='stop loss')

        freq_aggregated_df = pd.merge(freq_aggregated_df.copy(), av_dd_df.copy(),
                                      left_on='STRATPARAMS', right_index=True)
        freq_aggregated_df = pd.merge(freq_aggregated_df.copy(), qt_gain_df.copy(),
                                      left_on='STRATPARAMS', right_index=True)

        ######## computing metrics around strats and epochs
        freq_aggregated_df = freq_aggregated_df.rename(columns={
            'date': 'date',
            'epoch_number': 'epoch',
            'long_expo': 'long risk allocation',
            'short_expo': 'short risk allocation',
            'COMPO': 'composition',
            'simple_return': 'epoch realized return',
            'annual_return': 'epoch realized annualized return',
            'annual_volatility': 'epoch realized annualized volatility',
            'sharpe': 'epoch realized sharpe ratio',
            'calmar': 'epoch realized calmar ratio',
            'mdd': 'epoch realized max drawdown',
            'STRAT': 'strategy',
            'STRATPARAMS': 'strategy parameters',
            'subscription_asset': 'subscription asset'})
        freq_aggregated_df = freq_aggregated_df[
            ['date', 'strategy', 'strategy parameters', 'subscription asset', 'composition',
             'epoch', 'long risk allocation', 'short risk allocation', 'stop loss', 'take profit',
             'epoch realized return', 'epoch realized annualized return',
             'epoch realized annualized volatility',
             'epoch realized sharpe ratio', 'epoch realized calmar ratio',
             'epoch realized max drawdown']]

        freq_aggregated_df = freq_aggregated_df.sort_values(by='epoch')

        new_epoch_details = freq_aggregated_df.iloc[-1].copy()
        new_epoch_details_dict = new_epoch_details.to_dict()
        new_epoch_details_dict['date'] = str(new_epoch_details_dict['date'])

        compo_dic = new_epoch_details_dict['composition']
        clean_compo = {}
        for key, value in compo_dic.items():
            clean_compo[key] = f'{round(value * 100, 2)}%'

        new_epoch_details_dict['composition'] = clean_compo

        payload_message = json.dumps(new_epoch_details_dict)

        payload_message = payload_message.replace('"', '')

        date = new_epoch_details_dict['date']
        strat = new_epoch_details_dict['strategy']
        params = new_epoch_details_dict['strategy parameters']
        sub_ass = new_epoch_details_dict['subscription asset']
        composition = new_epoch_details_dict['composition']
        epoch = new_epoch_details_dict['epoch']
        lr = new_epoch_details_dict['long risk allocation']
        sr = new_epoch_details_dict['short risk allocation']
        sl = new_epoch_details_dict['stop loss']
        tp = new_epoch_details_dict['take profit']


        if plot_metrics:
            to_plot_df = freq_aggregated_df[
                ['epoch realized return', 'epoch realized max drawdown']].copy()
            fig = realtime_plotting_utility.plot_multiple_bar_series(
                data_df=to_plot_df[['epoch realized return']] * 100.,
                logy=False, split=False,
                put_on_same_scale=False,
                title=f'epoch realized return in percent (exposition moderating factor {moderating_factor}  epoch frequency {frequency})')
            fig.show()
            fig = realtime_plotting_utility.plot_multiple_bar_series(
                data_df=to_plot_df[['epoch realized max drawdown']] * 100.,
                logy=False, split=False,
                put_on_same_scale=False,
                title=f'epoch realized max drawdown in percent (exposition moderating factor {moderating_factor}  epoch frequency {frequency})')
            fig.show()
        freq_aggregated_df['year'] = freq_aggregated_df.index.year
        freq_aggregated_df['month'] = freq_aggregated_df.index.month


        def rename_month(row):
            if row['month'] == 1:
                return 'January'
            if row['month'] == 2:
                return 'February'
            if row['month'] == 3:
                return 'March'
            if row['month'] == 4:
                return 'April'
            if row['month'] == 5:
                return 'May'
            if row['month'] == 6:
                return 'June'
            if row['month'] == 7:
                return 'July'
            if row['month'] == 8:
                return 'August'
            if row['month'] == 9:
                return 'September'
            if row['month'] == 10:
                return 'October'
            if row['month'] == 11:
                return 'November'
            if row['month'] == 12:
                return 'December'

        freq_aggregated_df['month'] = freq_aggregated_df.apply(rename_month, axis=1)
        freq_aggregated_df = freq_aggregated_df.set_index(['year', 'month'])
        freq_aggregated_df = freq_aggregated_df.drop(columns=['date', 'epoch'])



        if write_excel_file:
            writer = pd.ExcelWriter(local_root_directory + f'{moderating_factor}_{universe_literal}_weekly_ls_epochs_details_ls.xlsx',
                                    engine='xlsxwriter')
            freq_aggregated_df.to_excel(writer, sheet_name='epoch')
            writer.save()

            writer = pd.ExcelWriter(
                local_root_directory + f'{moderating_factor}_{universe_literal}_kpi_df_ls_strategy.xlsx',
                engine='xlsxwriter')
            # whole_period_kpi_df.to_excel(writer, sheet_name=frequency)
            btd_kpis = btd_kpis.to_frame()
            btd_kpis.columns = [me_strat]
            past_returns = past_returns.to_frame()
            past_returns.columns = [me_strat]

            btd_kpis.to_excel(writer, sheet_name='advanced_btd')
            ytd_kpis.to_excel(writer, sheet_name='advanced_ytd')
            past_returns.to_excel(writer, sheet_name='common')
            writer.save()

    return payload_message


