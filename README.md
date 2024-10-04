# sh

### Gen SSH Key
```
ssh-keygen -f ~/ssh-key-ecdsa -t ecdsa -b 521
```
```
ssh-keygen -f ~/ssh-key-rsa -t rsa -b 4096
```
### Copy SSH Key to remote server
```
ssh-copy-id [-f] [-n] [-i identity file] [-p port] [-o ssh_option] [user@]hostname
```
