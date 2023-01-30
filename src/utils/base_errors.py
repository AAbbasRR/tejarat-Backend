from django.utils.translation import gettext as _


class BaseErrors:
    # system
    url_not_found = _('URL Not Found.')
    server_error = _('Server Error.')
    
    # register or fill profile
    user_must_have_email = _('User Must Have Email.')
    user_must_have_password = _('User Must Have Password.')
    invalid_mobile_number_format = _('Invalid Mobile Number Format.')
    user_account_with_email_exists = _('User Account With Email Exists.')
    user_account_with_national_code_exists = _('User Account With National Code Exists.')
    
    # login
    invalid_email_or_password = _('Invalid Email or Password.')
    user_account_not_active = _('User Account Not Active.')
    
    # forget password
    passwords_did_not_match = _('Password And Repeat Password Did Not Match.')
    user_dont_have_forget_password_permission = _('You Do Not Have Access To Change The Password, Please Try Again First Step.')
    
    # useful
    user_not_found = _('User Not Found')
    otp_code_expired = _('OTP Code Expired, Please Try To Resend New OTP Code.')
    invalid_otp_code = _('Invalid OTP Code, Please Try Again.')
    otp_code_has_already_been_sent = _('OTP Code Has Already Been Sent.')
    
    # store
    attempted_to_create_a_match_object_where_original_store_destination_store = _('Attempted To Create a Match Object Where original_store == destination_store')
    
    # machine
    machine_cant_imperfect_and_have_complete_cables = _('Machine Cant Imperfect And Have Complete Cables')
