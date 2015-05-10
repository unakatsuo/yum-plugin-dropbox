from yum import config
from yum.plugins import PluginYumExit, TYPE_INTERACTIVE

requires_api_version = '2.4'
plugin_type = (TYPE_INTERACTIVE)

def config_hook(conduit):
    config.RepoConf.dropbox_access_token = config.Option()

def init_hook(conduit):
    for repo in conduit.getRepos().listEnabled():
        for url in repo.baseurl:
            if not url.startswith('https://api-content.dropbox.com/1/files/auto/'): 
                continue
            if not repo.dropbox_access_token:
                raise PluginYumExit("dropbox_access_token parameter is unset")
            repo.http_headers["Authorization"]="Bearer " + repo.dropbox_access_token
