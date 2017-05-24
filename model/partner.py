# -*- coding: utf-8 -*-

from openerp import fields, models, api

class PartnerCurr(models.Model):
	_inherit = 'res.partner'

	course_ids = fields.Many2many('openacademy.course',string="Courses",default='course_ids_refresh',compute='course_ids_refresh',store=True)

	@api.depends('course_ids')
	def course_ids_refresh(self):
		import pdb; pdb.set_trace()
		cursos = [] 
		#self.course_ids = self.env['openacademy.sesion'].filtered(lambda s: self.partner.id  in s.atendee_ids).mapped('course_id')
		for sesion in self.env['openacademy.sesion']:
			if self.id in sesion.atendee_ids:
				cursos.append(sesion.course_id)
		self.course_ids = cursos		





