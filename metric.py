import pandas as pd
from huggingface_hub import hf_hub_download

def _metric(solution_df,submission_df, mode = "top_level", admin = False):
    """
    This function calculates the accuracy of the generated predictions.

    Parameters
    ----------
    solution_df : pandas.DataFrame
        The dataframe containing the solution data.
    submission_df : pandas.DataFrame
        The dataframe containing the submission data.
    mode : str, optional
        The mode of evaluation. Can be "top_level" or "bottom_level". The default is "top_level".
    
    Returns
    -------
    None.
    """


    solution_df["submission_pred"] = submission_df["pred"]
   
    if admin:
        source_col = "source_og"
    else:
        source_col = "source"

    
    cols = ["split","pred", source_col]


    solution_df["correct"] = solution_df["pred"] == solution_df["submission_pred"]
    accuracy = solution_df.groupby(cols)["correct"].mean().to_frame("accuracy").reset_index()
    accuracy["score_name"] = accuracy["pred"] +"_"+ accuracy[source_col]
    
    evaluation = {}
    
    split = "public"
    
    temp = accuracy.query(f"split=='{split}'")
    scores_by_source = temp.set_index("score_name")["accuracy"].sort_index()
    scores_by_source["generated_accuracy"] = temp.query("pred=='generated'")["accuracy"].mean()
    scores_by_source["pristine_accuracy"] = temp.query("pred=='pristine'")["accuracy"].mean()
    scores_by_source["balanced_accuracy"] = (scores_by_source["generated_accuracy"] + scores_by_source["pristine_accuracy"])/2.
    
    
    if mode == "top_level":
        scores_to_save = ["generated_accuracy", "pristine_accuracy", "balanced_accuracy"]
        evaluation[f"{split}_score"] = scores_by_source.loc[scores_to_save].to_dict()
    else:
        evaluation[f"{split}_score"] = scores_by_source.to_dict()

    split = "private"
    # private has everything

    temp = accuracy
    scores_by_source = temp.set_index("score_name")["accuracy"].sort_index()
    scores_by_source["generated_accuracy"] = temp.query("pred=='generated'")["accuracy"].mean()
    scores_by_source["pristine_accuracy"] = temp.query("pred=='pristine'")["accuracy"].mean()
    scores_by_source["balanced_accuracy"] = (scores_by_source["generated_accuracy"] + scores_by_source["pristine_accuracy"])/2.
    
    if mode == "top_level":
        scores_to_save = ["generated_accuracy", "pristine_accuracy", "balanced_accuracy"]
        evaluation[f"{split}_score"] = scores_by_source.loc[scores_to_save].to_dict()
    else:
        evaluation[f"{split}_score"] = scores_by_source.to_dict()
    

    if "time" in submission_df.columns:
        solution_df["submission_time"] = submission_df["time"]
        
        split = "public"
        evaluation[f"{split}_score"]["total_time"] = float(solution_df.query(f"split=='{split}'")["submission_time"].sum())

        split = "private"
        evaluation[f"{split}_score"]["total_time"] = float(solution_df["submission_time"].sum())
    else:
        for split in ["public","private"]:
            evaluation[f"{split}_score"]["total_time"] = -1


    if "score" in submission_df.columns:
        solution_df["submission_score"] = submission_df["score"]
    
        split = "public"
        evaluation[f"{split}_score"]["fail_rate"] = float(solution_df.query(f"split=='{split}'")["submission_score"].isna().mean())

        split = "private"
        evaluation[f"{split}_score"]["fail_rate"] = float(solution_df["submission_score"].isna().mean())

    else:
        for split in ["public","private"]:
            evaluation[f"{split}_score"]["fail_rate"] = -1



    return evaluation



def compute(params):
    solution_file = hf_hub_download(
        repo_id=params.competition_id,
        filename="solution.csv",
        token=params.token,
        repo_type="dataset",
    )

    solution_df = pd.read_csv(solution_file).set_index(params.submission_id_col)

    submission_filename = f"submissions/{params.team_id}-{params.submission_id}.csv"
    submission_file = hf_hub_download(
        repo_id=params.competition_id,
        filename=submission_filename,
        token=params.token,
        repo_type="dataset",
    )
    
    submission_df = pd.read_csv(submission_file).set_index(params.submission_id_col)

    return _metric(solution_df,submission_df)