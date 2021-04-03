# githubhosts_auto_updater

Update hosts to access GitHub in China

# Usage

### By yourself

`python githubhosts_auto_updater.py`

### Auto

1. Install `Crontab` .(You can check this by `crontab -l `, nothing appears is normal.)

2. Download the script to somewhere you like, such as 

   ```shell
   wget -P ~/.githubhosts_auto_updater/ https://raw.fastgit.org/F-Unction/githubhosts_auto_updater/main/githubhosts_auto_updater.py
   ```

3. Make it run by itself, such as

   ```shell
   sudo sh -c 'echo "0 * * * * python ~/.githubhosts_auto_updater/githubhosts_auto_updater.py" >> /etc/crontab'
   ```

   
