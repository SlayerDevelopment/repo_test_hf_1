from huggingface_hub import HfApi

if __name__ == "__main__":
    api = HfApi()
    # api.create_repo(repo_id="repo_test_hf_1")
    api.upload_file(
        path_or_fileobj="/home/bryan/huggin_face/repo_test_hf_1/README.md",
        path_in_repo="README.md",
        repo_id="thebryanalvarado/repo_test_hf_1",
    )
