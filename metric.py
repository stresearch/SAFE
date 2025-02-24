import pandas as pd
from huggingface_hub import hf_hub_download


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

    solution_df["submission_pred"] = submission_df["pred"]
    
    cols = ["split","pred","source"]


    solution_df["correct"] = solution_df["pred"] == solution_df["submission_pred"]
    accuracy = solution_df.groupby(cols)["correct"].mean().to_frame("accuracy").reset_index()
    accuracy["score_name"] = accuracy["pred"] +"_"+ accuracy["source"]
    
    evaluation = {}
    
    # for split,temp in accuracy.groupby("split"):
    #     scores_by_source = temp.set_index("score_name")["accuracy"].sort_index()
    #     scores_by_source["generated_mean"] = temp.query("pred=='generated'")["accuracy"].mean()
    #     scores_by_source["pristine_mean"] = temp.query("pred=='pristine'")["accuracy"].mean()
    #     scores_by_source["balanced_accuracy"] = (scores_by_source["generated_mean"] + scores_by_source["pristine_mean"])/2.
    #     evaluation[f"{split}_score"] = scores_by_source.to_dict()
        
    # for split,temp in accuracy.groupby("split"):
    scores_by_source = accuracy.set_index("score_name")["accuracy"].sort_index()
    scores_by_source["generated_mean"] = accuracy.query("pred=='generated'")["accuracy"].mean()
    scores_by_source["pristine_mean"] = accuracy.query("pred=='pristine'")["accuracy"].mean()
    scores_by_source["balanced_accuracy"] = (scores_by_source["generated_mean"] + scores_by_source["pristine_mean"])/2.
    evaluation["private_score"] = scores_by_source.to_dict()
    evaluation["public_score"] = scores_by_source.to_dict()
        
    # evaluation = {
    #     "public_score": {
    #         "metric1": public_score,
    #     },
    #     "private_score": {
    #         "metric1": public_score,
    #     }
    # }
    return evaluation