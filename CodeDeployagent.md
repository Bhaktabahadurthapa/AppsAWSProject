### Install the CodeDeploy agent for Ubuntu Server

To install the CodeDeploy agent on Ubuntu Server
Enter the following commands

sudo apt update
```bash
sudo apt update
```
```
sudo apt install ruby-full
```
```
sudo apt install wget
```
```
cd /home/ubuntu
```
```
wget https://bucket-name.s3.region-identifier.amazonaws.com/latest/install
```
bucket-name is the name of the Amazon S3 bucket that contains the CodeDeploy Resource Kit files for your region, and region-identifier is the identifier for your region.

For example:

https://aws-codedeploy-us-east-2.s3.us-east-2.amazonaws.com/latest/install

For a list of bucket names and region identifiers, see Resource kit bucket names by Region.https://docs.aws.amazon.com/codedeploy/latest/userguide/resource-kit.html#resource-kit-bucket-names
```
chmod +x ./install
```
Do one of the following:

To install the latest version of the CodeDeploy agent on any supported version of Ubuntu Server except 20.04:
```
sudo ./install auto
```
To check that the service is running

```
systemctl status codedeploy-agent
```
More:
Follow the AWS Documentation : https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ubuntu.html


