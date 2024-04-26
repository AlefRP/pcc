from priv_ad import Admin
    
administrator = Admin("admin", "admin@example.com", "123 Main St", [1, 2, 3, 4])
administrator.privileges.show_privileges()