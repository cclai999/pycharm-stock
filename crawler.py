import pandas as pd


def get_sum(df, op_title):
    roedf = df[df[0] == op_title].iloc[0][1:5].astype(float)
    roe = roedf.sum()
    return roe


def get_tab(url):
    dfs = pd.read_html(url)
    df = dfs[2]
    return df


def get_roe(stock_no=2330):
    url = f"http://jsjustweb.jihsun.com.tw/z/zc/zcr/zcr0.djhtm?b=Q&a={stock_no}"
    df = get_tab(url)
    title = "ROE(A)─稅後"
    roe = get_sum(df, title)
    return roe


def get_free_cashflow(stock_no=2330):
    url = f"http://jsjustweb.jihsun.com.tw/z/zc/zc30.djhtm?b=Q&a={stock_no}"
    df = get_tab(url)
    op_title = "來自營運之現金流量"
    op_cashflow_sum = get_sum(df, op_title)

    inv_title = "投資活動之現金流量"
    inv_cashflow_sum = get_sum(df, inv_title)

    free_cashflow = op_cashflow_sum + inv_cashflow_sum
    return free_cashflow


if __name__ == '__main__':
    print(get_roe())
    print(get_free_cashflow())
