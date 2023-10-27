#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from repository import Repository
from cdktf_cdktf_provider_github import repositoryCDK      

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here

        p = provider.GithubProvider(
            scope=scope,
            id="svg153_org",
            organization="svg153_org"
        )

        r_to_cdk = []
        for repo in ["github-as-code-cdk", "github-as-code-cdk-2"]:
            r = repository.Repository(
                scope=scope,
                id=repo,
                provider=p,
                name=repo,
                auto_init=True,
                visibility="internal"
            )
            r_to_cdk.append(r)
        
        
        cdk_repos = []
        for repo in r_to_cdk:
            r = repositoryCDK.RepositoryCDK(
                scope=scope,
                id=repo.name,
                name = name,
                allow_auto_merge = allow_auto_merge,
                allow_merge_commit = allow_merge_commit,
                allow_rebase_merge = allow_rebase_merge,
                allow_squash_merge = allow_squash_merge,
                allow_update_branch = allow_update_branch,
                archived = archived,
                archive_on_destroy = archive_on_destroy,
                auto_init = auto_init,
                default_branch = default_branch,
                delete_branch_on_merge = delete_branch_on_merge,
                description = description,
                gitignore_template = gitignore_template,
                has_discussions = has_discussions,
                has_downloads = has_downloads,
                has_issues = has_issues,
                has_projects = has_projects,
                has_wiki = has_wiki,
                homepage_url = homepage_url,
                id = id,
                ignore_vulnerability_alerts_during_read = ignore_vulnerability_alerts_during_read,
                is_template = is_template,
                license_template = license_template,
                merge_commit_message = merge_commit_message,
                merge_commit_title = merge_commit_title,
                pages = pages,
                private = private,
                security_and_analysis = security_and_analysis,
                squash_merge_commit_message = squash_merge_commit_message,
                squash_merge_commit_title = squash_merge_commit_title,
                template = template,
                topics = topics,
                visibility = visibility,
                vulnerability_alerts = vulnerability_alerts
            )
            
            cdk_repos.append(r)
            

app = App()

MyStack(app, "github-as-code-cdk")

app.synth()
