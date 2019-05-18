  except Exception as err:
        with open('control_Computer_by_mail.txt','a') as f:
            f.write(logging.error('damn!', exc_info= True))