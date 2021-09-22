from sscutils import create_trepo_with_subsets

comments_table = create_trepo_with_subsets("comments", group_cols='topic')
users_table = create_trepo_with_subsets("users")
