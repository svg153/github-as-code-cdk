#!/usr/bin/env python

class Repository:
    def __init__(self,
            name: str,
            allow_auto_merge: typing.Union[bool, IResolvable] = None,
            allow_merge_commit: typing.Union[bool, IResolvable] = None,
            allow_rebase_merge: typing.Union[bool, IResolvable] = None,
            allow_squash_merge: typing.Union[bool, IResolvable] = None,
            allow_update_branch: typing.Union[bool, IResolvable] = None,
            archived: typing.Union[bool, IResolvable] = None,
            archive_on_destroy: typing.Union[bool, IResolvable] = None,
            auto_init: typing.Union[bool, IResolvable] = None,
            default_branch: str = None,
            delete_branch_on_merge: typing.Union[bool, IResolvable] = None,
            description: str = None,
            gitignore_template: str = None,
            has_discussions: typing.Union[bool, IResolvable] = None,
            has_downloads: typing.Union[bool, IResolvable] = None,
            has_issues: typing.Union[bool, IResolvable] = None,
            has_projects: typing.Union[bool, IResolvable] = None,
            has_wiki: typing.Union[bool, IResolvable] = None,
            homepage_url: str = None,
            id: str = None,
            ignore_vulnerability_alerts_during_read: typing.Union[bool, IResolvable] = None,
            is_template: typing.Union[bool, IResolvable] = None,
            license_template: str = None,
            merge_commit_message: str = None,
            merge_commit_title: str = None,
            pages: RepositoryPages = None,
            private: typing.Union[bool, IResolvable] = None,
            security_and_analysis: RepositorySecurityAndAnalysis = None,
            squash_merge_commit_message: str = None,
            squash_merge_commit_title: str = None,
            template: RepositoryTemplate = None,
            topics: typing.List[str] = None,
            visibility: str = None,
            vulnerability_alerts: typing.Union[bool, IResolvable] = None
        ):
        self.name = name
        self.allow_auto_merge = allow_auto_merge
        self.allow_merge_commit = allow_merge_commit
        self.allow_rebase_merge = allow_rebase_merge
        self.allow_squash_merge = allow_squash_merge
        self.allow_update_branch = allow_update_branch
        self.archived = archived
        self.archive_on_destroy = archive_on_destroy
        self.auto_init = auto_init
        self.default_branch = default_branch
        self.delete_branch_on_merge = delete_branch_on_merge
        self.description = description
        self.gitignore_template = gitignore_template
        self.has_discussions = has_discussions
        self.has_downloads = has_downloads
        self.has_issues = has_issues
        self.has_projects = has_projects
        self.has_wiki = has_wiki
        self.homepage_url = homepage_url
        self.id = id
        self.ignore_vulnerability_alerts_during_read = ignore_vulnerability_alerts_during_read
        self.is_template = is_template
        self.license_template = license_template
        self.merge_commit_message = merge_commit_message
        self.merge_commit_title = merge_commit_title
        self.pages = pages
        self.private = private
        self.security_and_analysis = security_and_analysis
        self.squash_merge_commit_message = squash_merge_commit_message
        self.squash_merge_commit_title = squash_merge_commit_title
        self.template = template
        self.topics = topics
        self.visibility = visibility
        self.vulnerability_alerts = vulnerability_alerts

    def to_dict(self):
        return {
            "name": self.name,
            "allow_auto_merge": self.allow_auto_merge,
            "allow_merge_commit": self.allow_merge_commit,
            "allow_rebase_merge": self.allow_rebase_merge,
            "allow_squash_merge": self.allow_squash_merge,
            "allow_update_branch": self.allow_update_branch,
            "archived": self.archived,
            "archive_on_destroy": self.archive_on_destroy,
            "auto_init": self.auto_init,
            "default_branch": self.default_branch,
            "delete_branch_on_merge": self.delete_branch_on_merge,
            "description": self.description,
            "gitignore_template": self.gitignore_template,
            "has_discussions": self.has_discussions,
            "has_downloads": self.has_downloads,
            "has_issues": self.has_issues,
            "has_projects": self.has_projects,
            "has_wiki": self.has_wiki,
            "homepage_url": self.homepage_url,
            "id": self.id,
            "ignore_vulnerability_alerts_during_read": self.ignore_vulnerability_alerts_during_read,
            "is_template": self.is_template,
            "license_template": self.license_template,
            "merge_commit_message": self.merge_commit_message,
            "merge_commit_title": self.merge_commit_title,
            "pages": self.pages,
            "private": self.private,
            "security_and_analysis": self.security_and_analysis,
            "squash_merge_commit_message": self.squash_merge_commit_message,
            "squash_merge_commit_title": self.squash_merge_commit_title,
            "template": self.template,
            "topics": self.topics,
            "visibility": self.visibility,
            "vulnerability_alerts": self.vulnerability_alerts
        }

    def __repr__(self):
        return f"Repository({self.to_dict()})"

    def __str__(self):
        return f"Repository({self.to_dict()})"

    @staticmethod
    def from_dict(d):
        return Repository(**d)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.to_dict() == other.to_dict()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.to_dict())

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, sort_keys=True, default=str)

    @staticmethod
    def from_json(json_str):
        return Repository.from_dict(json.loads(json_str, parse_float=str, parse_int=str, parse_constant=str))

    def to_yaml(self):
        return yaml.dump(self.to_dict(), sort_keys=True)

    @staticmethod
    def from_yaml(yaml_str):
        return Repository.from_dict(yaml.safe_load(yaml_str))
