import time
import logging
import boto.ec2

SG_NAME = 'Scrapyd'
SG_DESCRIPTION = 'Scrapy daemon'
USER_DATA_FILE = 'user_data-scrapyd.sh'
AMI='ami-da0d9eb3' # Find others AMI on http://cloud-images.ubuntu.com/locator/ec2
KEY_NAME='main'
INSTANCE_TYPE='t1.micro'
SECURITY_GROUPS=[SG_NAME]

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
conn = boto.ec2.connect_to_region("us-east-1")

logging.info("Checking security group for EC2 instance...")
sgroups = [sg.name for sg in conn.get_all_security_groups()]
if not SG_NAME in sgroups:
    logging.info("Creating group %s..." % SG_NAME)
    conn.create_security_group(SG_NAME, SG_DESCRIPTION)
    logging.info("Adding rules to security group...")
    conn.authorize_security_group(SG_NAME, ip_protocol='tcp', from_port='22', to_port='22', cidr_ip='0.0.0.0/0')
    conn.authorize_security_group(SG_NAME, ip_protocol='tcp', from_port='6800', to_port='6800', cidr_ip='0.0.0.0/0')

with open(USER_DATA_FILE) as f:
    user_data = f.read()

logging.info("Running instance...")
reservation = conn.run_instances(AMI, user_data=user_data, key_name=KEY_NAME, instance_type=INSTANCE_TYPE, security_groups=SECURITY_GROUPS)
instance = reservation.instances[0]
while instance.state != 'running':
    time.sleep(10)
    instance.update()
logging.info("Point your browser to http://%s:6800 it should show the Scrapyd web UI." % instance.public_dns_name)
