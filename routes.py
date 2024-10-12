from core.state import Auth
from core.router import Route, Router, Callback
from core.utils import return_valid_access_manu as MMM

router = Router(Route("Main", description="Maktab 112 - Pharmacy Management",
                      children=[Route("Login", condition=lambda: Auth.login_status is False,
                                      callback=Callback('admin.callbacks', 'login')
                                      ),
                                Route(
                                    "Register",
                                    condition=lambda: Auth.login_status is False,
                                    callback=Callback('admin.callbacks', 'register')
                                ),
                                Route('Shop Pharmacy', children=[
                                    Route('Buy',
                                          callback=Callback('admin.callbacks', 'Buy_Shop')),
                                    Route('Please for payment in login or register',
                                          condition=lambda: Auth.login_status is False and Auth.zanbil),

                                    Route('Payment', condition=(lambda: Auth.login_status),
                                          callback=Callback('admin.callbacks', 'Payment')),
                                ]),

                                Route(
                                    "Access ",
                                    condition=(lambda: Auth.login_status and MMM('access',
                                                                                 Auth.user_register)),
                                    children=[
                                        Route('Add Access', callback=Callback('admin.callbacks', 'set_access'),
                                              condition=(lambda: Auth.login_status and MMM('add_access',
                                                                                           Auth.user_register))),
                                        Route('Remove Access', callback=Callback('admin.callbacks', 'remove_access'),
                                              condition=(lambda: Auth.login_status and MMM('remove_access',
                                                                                           Auth.user_register))),
                                        Route('User Access', children=[
                                            Route('Add Access User',
                                                  callback=Callback('admin.callbacks', 'update_access_user'),
                                                  condition=(lambda: Auth.login_status and MMM('user_access',
                                                                                               Auth.user_register))),
                                            Route('Remove Access User',
                                                  callback=Callback('admin.callbacks', 'remove_access_user'),
                                                  condition=(lambda: Auth.login_status and MMM('remove_access_user',
                                                                                               Auth.user_register))),
                                        ]),
                                        Route('Drug Access',
                                              condition=(lambda: Auth.login_status and MMM('drug_access',
                                                                                           Auth.user_register)),
                                              children=[
                                                  Route('Add Access Drug',
                                                        callback=Callback('admin.callbacks', 'update_access_drug'),
                                                        condition=(lambda: Auth.login_status and MMM('add_access_drug',
                                                                                                     Auth.user_register))),
                                                  Route('Remove Access Drug',
                                                        callback=Callback('admin.callbacks', 'remove_access_drug'),
                                                        condition=(
                                                            lambda: Auth.login_status and MMM('remove_access_drug',
                                                                                              Auth.user_register))),
                                              ]),
                                        Route('Menu Access',
                                              condition=(lambda: Auth.login_status and MMM('menu_access',
                                                                                           Auth.user_register)),
                                              children=[
                                                  Route('Add  Menu',
                                                        callback=Callback('admin.callbacks', 'set_access_menu')),
                                                  Route('Add Access Menu',
                                                        callback=Callback('admin.callbacks', 'add_access_menu')),
                                                  Route('remove Access Menu',
                                                        callback=Callback('admin.callbacks', 'remove_access_menu'))

                                              ]),

                                    ]),

                                Route(
                                    "Drug options",
                                    condition=(lambda: Auth.login_status and MMM('drug_options',
                                                                                 Auth.user_register)),
                                    children=[
                                        Route('Add Drug', callback=Callback('admin.callbacks', 'Add_drug'), condition=(
                                            lambda: Auth.login_status and MMM('add_drug',
                                                                              Auth.user_register))),
                                        Route('Remove Drug', callback=Callback('admin.callbacks', 'Remove_drug'),
                                              condition=(
                                                  lambda: Auth.login_status and MMM('remove_drug',
                                                                                    Auth.user_register))),
                                        Route('Update Cont Drug',
                                              callback=Callback('admin.callbacks', 'Update_drug_cont'), condition=(
                                                lambda: Auth.login_status and MMM('update_cont_drug',
                                                                                  Auth.user_register))),
                                        Route('Change Drug Price',
                                              callback=Callback('admin.callbacks', 'change_drug_price'), condition=(
                                                lambda: Auth.login_status and MMM('change_drug_price',
                                                                                  Auth.user_register))),
                                        Route('Change Drug exp-date',
                                              callback=Callback('admin.callbacks', 'change_drug_exp'), condition=(
                                                lambda: Auth.login_status and MMM('change_drug_exp-date',
                                                                                  Auth.user_register))),
                                        Route('Drug print',
                                              callback=Callback('admin.callbacks', 'Drug_print'), condition=(
                                                lambda: Auth.login_status and MMM('drug_print',
                                                                                  Auth.user_register))),
                                        Route('Drug buy user',
                                              callback=Callback('admin.callbacks', 'box_access_user'), condition=(
                                                lambda: Auth.login_status and MMM('drug_buy_user',
                                                                                  Auth.user_register))),

                                    ]),
                                Route(
                                    "Logout",
                                    condition=lambda: Auth.login_status,
                                    callback=Callback('admin.callbacks', 'logout')
                                ),
                                Route("Panel",
                                      condition=lambda: Auth.login_status,
                                      children=[
                                          Route("Login", callback=Callback('admin.callbacks', 'login')),
                                          Route("Register", callback=Callback('admin.callbacks', 'register')),
                                          Route("In Panel", children=[
                                              Route("Login", callback=Callback('admin.callbacks', 'login')),
                                              Route("hamid", callback=Callback('admin.callbacks', 'register')),
                                          ]),
                                      ]),
                                ])
                )
