from . import models


def _pre_init_hook_set_new_expiration_date(cr):
    """After installing set new expiration date
    """
    cr.execute("""ALTER TABLE account_move
                ADD COLUMN IF NOT EXISTS new_expiration_date TIMESTAMP WITHOUT TIME ZONE""")
    query = '''
        UPDATE account_move
        SET new_expiration_date = 
            CASE
                WHEN invoice_date_due IS NOT NULL THEN
                    invoice_date_due
                WHEN date IS NOT NULL THEN
                    date
                ELSE
                    NULL
            END;
        '''
    cr.execute(query)
