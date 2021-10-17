from re import sub
from sscutils import dump_dfs_to_trepos
from .trepos import comments_table, users_table

blue_chip_ids = {
    'MOLly tulajok topikja': 5535,
    'OTP részvényesek ide!': 5224,
    'Mol tulajok normálisan': 38965,
    'Richter topik': 6389,
    'mtelekom': 6428
}

def create_subsets(subset_name, only_hun_bluechip = False):
    """create subsets that are described in the config of the repo
    
    only_hun_bluechip: bool -> Only a subset of hungarian bluechip stocks
    """
    if subset_name == "complete":
        return
    comments_df = comments_table.get_full_df().loc[lambda df: df['topic_id'].isin(blue_chip_ids.values()) & only_hun_bluechip]
    users_df = users_table.get_full_df()

    dump_dfs_to_trepos(subset_name, [(comments_df, comments_table), (users_df, users_table)])