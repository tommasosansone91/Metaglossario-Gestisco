
command `sudo systemctl start mybig_app` holds on and service stands in status loaded(activating) never turning to active

    sudo systemctl restart metaglossario_gestisco.service

does not end, and the app does not start up.

When you use Type=notify systemd waits for a notification from the service via sd_notify, support for this was only added in Gunicorn in version 20.0 (See the following comment on a GitHub issue).

If you do want to use Type=notify you should upgrade your Gunicorn version, otherwise you can simply set Type=exec

https://stackoverflow.com/a/78454566/7658051
