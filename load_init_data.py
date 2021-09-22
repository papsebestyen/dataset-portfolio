import sys
import pandas as pd
from sscutils import dump_dfs_to_trepos
from src.trepos import comments_table, users_table

if __name__ == "__main__":

    droot = sys.argv[1]
    
    comments_df = pd.read_csv(f"{droot}/comments.csv", encoding='utf-8')
    users_df = pd.read_csv(f"{droot}/users.csv", encoding='utf-8')

    dump_dfs_to_trepos(None, [(comments_df, comments_table), (users_df, users_table)])