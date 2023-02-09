# Big Data Ecosystem

## Lab 1: Setting up the connection to Adaltas Cloud

### Context

The Hadoop cluster that you will be using for this class is located on Adaltas Cloud that is on a private network only accessible through a VPN ([Virtual Private Network](https://en.wikipedia.org/wiki/Virtual_private_network)) tunnel. The VPN solution used is [OpenVPN](https://openvpn.net/).

### Prerequisites

You should have received an email from Adaltas containing a `.ovpn` file that you will use to open the connect via VPN:

1. Find the email (also check your “Spam” folder)
2. Download the .ovpn file

### VPN client installation

1. Depending on your OS, install the OpenVPN client:
   - On Windows, find the installer here: https://openvpn.net/vpn-client/
   - On Mac, you can use Tunnelblick : Use the official client https://openvpn.net/vpn-client/ (or TunnelBlick https://tunnelblick.net/)
   - On Linux, if you have Gnome, you can use the `networkmanager-openvpn` package. Otherwise, use your distribution package manager to install the openvpn package.
2. Import the `.ovpn` file to the client (the way to do so depends on your OS and your client, read the docs!)
3. Start the VPN connection
4. Test that everything is working by pinging the edge server:
   ```
   ping edge-1.au.adaltas.cloud
   ```

### Troubleshooting

If you encounter errors, before asking for help:

- Check the VPN client logs for errors. Use Google to understand what is going on!
- Check if you have a DNS issue, ping the edge server using its IP address instead of its FQDN: `ping 10.0.0.63`
- Check that your client is well installed

If still having trouble, contact your teacher via email using the tag `[ECE][VPN]` and attach:

- The client logs
- The results returned by the ping requests (via FQDN and IP)
- Any other information you find useful

### Connecting with SSH

To interact with the cluster, we will connect to the edge server in order to run commands. We will use the SSH (Secure SHell) protocol to open a shell on the edge server and write commands.
To connect via SSH:

1. On Windows only, you might have to install Putty: https://www.putty.org/
2. Check the email you received from Adaltas. You will find your username, password, and a sample SSH command there. My username is gauthier, this is the command I received:
   ```
   ssh gauthier@edge-1.au.adaltas.cloud
   ```
3. On your first connection, you will be asked to change your password. Read the instructions carefully: when you are prompted `Current password`, type the temporary password that you received by email. Please store your new password in a safe place.

### Linux commands

Now you will try out some Linux commands. Check out this tutorial: [The Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview).
Ultimately, you have to create a file in the folder that your teacher will give you. The file has to:

- Be named after your username with the extension `.txt` (e.g. `gauthier.txt`)
