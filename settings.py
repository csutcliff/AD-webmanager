class Settings:
    SECRET_KEY = "AHDGIWIWBQSBKQYUQXBXKGAsdhahdflkjfgierqhs"
    LDAP_DOMAIN = "cujae.edu.cu"
    SEARCH_DN = "dc=cujae,dc=edu,dc=cu"
    LDAP_SERVER = "10.8.1.125"
    DEBUG = True
    # URL_PREFIX = "/domain"
    TREE_BLACKLIST = ["CN=ForeignSecurityPrincipals", "OU=sudoers", "CN=Builtin", "CN=Infrastructure",
                      "CN=LostAndFound", "CN=Managed Service Accounts", "CN=NTDS Quotas", "CN=Program Data",
                      "CN=System", "OU=Domain Controllers"]
    SICCIP_AWARE = False
    EXTRA_FIELDS = True
    ADMIN_GROUP = "SM Admins"
    auth_admins = {'acarturodc': ['10.8.2.200'], 'acivan':['10.8.5.11','10.71.']}
    SEARCH_ATTRS = [('sAMAccountName', 'Usuario'), ('givenName', 'Nombre')]
