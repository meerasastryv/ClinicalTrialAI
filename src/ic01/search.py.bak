from models import Requirement


def find_by_product(requirements, product):

   return [
       req
       for req in requirements
       if req.product.upper() == product.upper()
   ]


def find_by_type(requirements, req_type):

   return [
       req
       for req in requirements
       if req.req_type.upper() == req_type.upper()
   ]


def find_by_keyword(requirements, keyword):

   keyword = keyword.lower()

   return [
       req
       for req in requirements
       if keyword in req.text.lower()
   ]


def find_by_link(requirements, requirement_id):

   return [
       req
       for req in requirements
       if requirement_id in req.links
   ]

