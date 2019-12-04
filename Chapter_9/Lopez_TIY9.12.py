from admin_privileges import Admin

admin_1 = Admin('Manuel', 'Lopez', 18, 'Fort Wayne', 'Male', 'can add post', 'can delete post')

admin_1.privileges.show_privileges()
