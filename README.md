## Put yum repository on your Dropbox

yum-plugin-dropbox allows yum to access to private yum repository on Dropbox.

### Install:

```
rpm -Uvh https://github.com/unakatsuo/yum-plugin-dropbox/releases/download/v0.1/yum-plugin-dropbox-0.1-1.el7.centos.noarch.rpm
```

### Setup:

Get your access token from [Dropbox App Console](https://www.dropbox.com/developers/apps).

1. Click ``Create App`` button then choose ``Dropbox API App``.
2. Once the app is created, there is a button in ``Generated access token``. New token string will appear after clicking.
3. Paste the generated token string to repo conf.

Put repo definition as ``/etc/yum.repos.d/dropbox.repo``. Note that ``baseurl`` must starts with ``https://api-content.dropbox.com/1/files/auto`` and ``dropbox_access_token`` parameter is required.

```
[Dropboxrepo]
name=Your Dropbox repo
baseurl=https://api-content.dropbox.com/1/files/auto/yum/
gpgcheck=0
enabled=1
dropbox_access_token=sHsF6gxJiwIXXXXXXXXXXXXCwE1Ei-XP6igylXXXXHH43lx_f8XbWmrknUWAJ7YO6Ms2
```
