from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, surname, name, pseudo, email, is_staff=False, password = None):
        
        if not surname:
            raise ValueError("User must have surname")
        if not name:
            raise ValueError("User must have name")
        if not pseudo:
            raise ValueError("User must have pseudo")
        if not email:
            raise ValueError("User must have email")

        email = self.normalize_email(email)
        user = self.model(surname=surname,
                          name=name,
                          pseudo=pseudo,
                          email=email,
                          is_staff=is_staff,
                         )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, surname, name, pseudo, email, password = None):
        user = self.create_user(surname, name, pseudo, email, password = password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user