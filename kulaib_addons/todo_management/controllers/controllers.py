# -*- coding: utf-8 -*-
# from odoo import http


# class TodoManagement(http.Controller):
#     @http.route('/todo_management/todo_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_management/todo_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_management.listing', {
#             'root': '/todo_management/todo_management',
#             'objects': http.request.env['todo_management.todo_management'].search([]),
#         })

#     @http.route('/todo_management/todo_management/objects/<model("todo_management.todo_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_management.object', {
#             'object': obj
#         })

