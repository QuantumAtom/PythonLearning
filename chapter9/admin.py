from userclass import Users
from adminclass import Admin, Privileges 

thorrezv = Admin('victor', 'thorrez', 'support admin', 'it', '!thorrezv', 0,)

thorrezv.privileges.access = ['reset password', 'unlock account', 'change group memberships']

thorrezv.privileges.show_privileges()