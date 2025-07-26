# basic import 
from mcp.server.fastmcp import FastMCP
import subprocess
import ssl
import socket
import datetime


# instantiate an MCP server client
mcp = FastMCP("Hello World")

# DEFINE TOOLS
@mcp.tool()
def ping(domain:str):
    """Ping a website"""
    out = subprocess.run(['ping', domain], capture_output=True)
    return(out.stdout.decode())

@mcp.tool()
def nmap_version(ip:str):
    """Run a Nmap version scan on website"""
    out = subprocess.run(['nmap -sV -p80', ip], capture_output=True)
    return(out.stdout.decode())

@mcp.tool()
def nmap_os_detection(ip: str):
    """Run a Nmap OS detection scan (-O)"""
    out = subprocess.run(['nmap', '-O', ip], capture_output=True, text=True)
    return out.stdout

@mcp.tool()
def nmap_quick_scan(ip: str):
    """Run a quick Nmap scan (-T4 -F)"""
    import subprocess
    out = subprocess.run(['nmap', '-T4', '-F', ip], capture_output=True, text=True)
    return out.stdout

@mcp.tool()
def get_ssl_cert_info(domain: str, port: int = 443):
        """Get SSL certificate for the given domain"""
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        return {
            "subject": dict(x[0] for x in cert['subject']),
            "issuer": dict(x[0] for x in cert['issuer']),
            "notBefore": cert['notBefore'],
            "notAfter": cert['notAfter'],
            "valid_from": datetime.datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z"),
            "valid_to": datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z"),
            "serialNumber": cert.get("serialNumber"),
        }


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
    
 
 # execute and return the stdio output
if __name__ == "__main__":
    mcp.run(transport="stdio")
