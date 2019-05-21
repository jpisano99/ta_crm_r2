from my_app import db

class Bookings(db.Model):
    __tablename__ = 'bookings'

    erp_end_customer_name = db.Column(db.String(100))
    total_bookings = db.Column(db.Float)
    product_id = db.Column(db.String(25))
    date_added = db.Column(db.DateTime)
    hash_value = db.Column(db.String(50), primary_key=True)


class Customers(db.Model):
    __tablename__ = 'customers'

    customer_erp_name = db.Column(db.String(100))
    customer_ultimate_name = db.Column(db.String(100))
    date_added = db.Column(db.DateTime)
    hash_value = db.Column(db.String(50), primary_key=True)

    # def __repr__(self):
    #    return "<name {}: '{} , {}'>".format(self.id, self.last_name,self.first_name,self.company_name)


class Services(db.Model):
    __tablename__ = 'services'

    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    as_sku = db.Column(db.String(45))
    date_added = db.Column(db.DateTime)


class Coverage(db.Model):
    __tablename__ = 'coverage'

    id = db.Column(db.Integer, primary_key=True)
    pss_name = db.Column(db.String(30))
    tsa_name = db.Column(db.String(30))
    sales_level_1 = db.Column(db.String(30))
    sales_level_2 = db.Column(db.String(30))
    sales_level_3 = db.Column(db.String(30))
    sales_level_4 = db.Column(db.String(30))
    sales_level_5 = db.Column(db.String(30))
    fiscal_year = db.Column(db.String(30))

    @staticmethod
    def newest():
        return Coverage.query.order_by(Coverage.pss_name).all()

    def get_page(page_num):
        num_of_pages = Coverage.query.paginate(per_page=10)
        return Coverage.query.order_by(Coverage.id).offset(page_num*10)

    def newest_name(num):
        return Coverage.query.order_by(Coverage.pss_name).limit(num)


print ('hello from models')

