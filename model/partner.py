# -*- coding: utf-8 -*-

from openerp import fields, models, api
from datetime import date

# Al elegir el TransientModel, se genera la tabla cada vez que se ve la vista, pero no queda permanente
class PartnerCurr(models.Model):
	_inherit = 'res.partner'

	course_ids = fields.Many2many('openacademy.course',string="Courses")

	@api.multi
	def course_ids_refresh(self):
		"""
		import pdb; pdb.set_trace()
		cursos = [] 
		for sesion in self.env['openacademy.session'].search([()]):
			if self <= sesion.attendee_ids:
				# cursos es una lista de Id, no es un datarecord
				# Habría que comprobar que no hay cursos duplicados
				cursos.append(sesion.course_id.id)
		 Aqui se hace un browsw implicito		
		self.course_ids = cursos		
		"""
		# Forma alternativa mas compacta
		# Se come una lista de Id's sin necesidad de hacer el browse		
		
		# courses_attended = conjunto del los course_ids en los que  el partner es attendant de alguna sesion
		courses_attended = []
		courses_pending  = []
		#import pdb; pdb.set_trace()
		courses_attended = set([sesion.course_id.id \
			for sesion in self.env['openacademy.session'].search([('id','>',0)]) \
				if self <= sesion.attendee_ids]) 
		""" Ahora filtro los courses en los que tiene alguna sesion pendiente 
			partner esta suscrito a todas las sesiones """
		# courses_pending = conjunto de los cursos de los que el partner es attendant de alguna sesion
		# 	pero con sesiones no finalizadas o en las qu el partner no esta inscrito
		courses_pending = set([sesion.course_id.id  \
			for course in courses_attended \
				for sesion in self.env['openacademy.session'].search([('course_id','=',course)])  \
					if fields.Date.from_string(sesion.end_date) >= date.today() \
					 or not self <= sesion.attendee_ids])
		""" Finalmente Calculo la diferencia """
		
		self.course_ids = courses_attended - courses_pending  

