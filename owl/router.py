class LogRouter:
    logger_db = 'logger'

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'owl':
            return 'logger'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'owl':
            return 'logger'
        return None

    def allow_syncdb(self, db, model):
        if db == 'logger':
            return model._meta.app_label == 'owl'
        elif model._meta.app_label == 'owl':
            return False
        return None
