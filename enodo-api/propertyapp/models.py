# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PropertyInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    full_address = models.TextField(db_column='Full Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    zip = models.IntegerField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.
    rec_type = models.TextField(db_column='REC_TYPE', blank=True, null=True)  # Field name made lowercase.
    pin = models.IntegerField(db_column='PIN', blank=True, null=True)  # Field name made lowercase.
    ovacls = models.IntegerField(db_column='OVACLS', blank=True, null=True)  # Field name made lowercase.
    class_description = models.TextField(db_column='CLASS_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    current_land = models.IntegerField(db_column='CURRENT_LAND', blank=True, null=True)  # Field name made lowercase.
    current_building = models.IntegerField(db_column='CURRENT_BUILDING', blank=True, null=True)  # Field name made lowercase.
    current_total = models.IntegerField(db_column='CURRENT_TOTAL', blank=True, null=True)  # Field name made lowercase.
    estimated_market_value = models.IntegerField(db_column='ESTIMATED_MARKET_VALUE', blank=True, null=True)  # Field name made lowercase.
    prior_land = models.IntegerField(db_column='PRIOR_LAND', blank=True, null=True)  # Field name made lowercase.
    prior_building = models.IntegerField(db_column='PRIOR_BUILDING', blank=True, null=True)  # Field name made lowercase.
    prior_total = models.IntegerField(db_column='PRIOR_TOTAL', blank=True, null=True)  # Field name made lowercase.
    pprior_land = models.IntegerField(db_column='PPRIOR_LAND', blank=True, null=True)  # Field name made lowercase.
    pprior_building = models.IntegerField(db_column='PPRIOR_BUILDING', blank=True, null=True)  # Field name made lowercase.
    pprior_total = models.IntegerField(db_column='PPRIOR_TOTAL', blank=True, null=True)  # Field name made lowercase.
    pprior_year = models.IntegerField(db_column='PPRIOR_YEAR', blank=True, null=True)  # Field name made lowercase.
    town = models.IntegerField(db_column='TOWN', blank=True, null=True)  # Field name made lowercase.
    volume = models.IntegerField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    loc = models.TextField(db_column='LOC', blank=True, null=True)  # Field name made lowercase.
    tax_code = models.IntegerField(db_column='TAX_CODE', blank=True, null=True)  # Field name made lowercase.
    neighborhood = models.IntegerField(db_column='NEIGHBORHOOD', blank=True, null=True)  # Field name made lowercase.
    houseno = models.IntegerField(db_column='HOUSENO', blank=True, null=True)  # Field name made lowercase.
    dir = models.TextField(db_column='DIR', blank=True, null=True)  # Field name made lowercase.
    street = models.TextField(db_column='STREET', blank=True, null=True)  # Field name made lowercase.
    suffix = models.TextField(db_column='SUFFIX', blank=True, null=True)  # Field name made lowercase.
    apt = models.TextField(db_column='APT', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    res_type = models.TextField(db_column='RES_TYPE', blank=True, null=True)  # Field name made lowercase.
    bldg_use = models.TextField(db_column='BLDG_USE', blank=True, null=True)  # Field name made lowercase.
    apt_desc = models.TextField(db_column='APT_DESC', blank=True, null=True)  # Field name made lowercase.
    comm_units = models.TextField(db_column='COMM_UNITS', blank=True, null=True)  # Field name made lowercase.
    ext_desc = models.TextField(db_column='EXT_DESC', blank=True, null=True)  # Field name made lowercase.
    full_bath = models.IntegerField(db_column='FULL_BATH', blank=True, null=True)  # Field name made lowercase.
    half_bath = models.IntegerField(db_column='HALF_BATH', blank=True, null=True)  # Field name made lowercase.
    bsmt_desc = models.TextField(db_column='BSMT_DESC', blank=True, null=True)  # Field name made lowercase.
    attic_desc = models.TextField(db_column='ATTIC_DESC', blank=True, null=True)  # Field name made lowercase.
    ac = models.IntegerField(db_column='AC', blank=True, null=True)  # Field name made lowercase.
    fireplace = models.IntegerField(db_column='FIREPLACE', blank=True, null=True)  # Field name made lowercase.
    gar_desc = models.TextField(db_column='GAR_DESC', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    building_sq_ft = models.IntegerField(db_column='BUILDING_SQ_FT', blank=True, null=True)  # Field name made lowercase.
    land_sq_ft = models.IntegerField(db_column='LAND_SQ_FT', blank=True, null=True)  # Field name made lowercase.
    bldg_sf = models.TextField(db_column='BLDG_SF', blank=True, null=True)  # Field name made lowercase.
    units_tot = models.TextField(db_column='UNITS_TOT', blank=True, null=True)  # Field name made lowercase.
    multi_sale = models.IntegerField(db_column='MULTI_SALE', blank=True, null=True)  # Field name made lowercase.
    deed_type = models.IntegerField(db_column='DEED_TYPE', blank=True, null=True)  # Field name made lowercase.
    sale_date = models.TextField(db_column='SALE_DATE', blank=True, null=True)  # Field name made lowercase.
    sale_amount = models.IntegerField(db_column='SALE_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    appcnt = models.IntegerField(db_column='APPCNT', blank=True, null=True)  # Field name made lowercase.
    appeal_a = models.IntegerField(db_column='APPEAL_A', blank=True, null=True)  # Field name made lowercase.
    appeal_a_status = models.TextField(db_column='APPEAL_A_STATUS', blank=True, null=True)  # Field name made lowercase.
    appeal_a_result = models.TextField(db_column='APPEAL_A_RESULT', blank=True, null=True)  # Field name made lowercase.
    appeal_a_reason = models.IntegerField(db_column='APPEAL_A_REASON', blank=True, null=True)  # Field name made lowercase.
    appeal_a_pin_result = models.TextField(db_column='APPEAL_A_PIN_RESULT', blank=True, null=True)  # Field name made lowercase.
    appeal_a_propav = models.IntegerField(db_column='APPEAL_A_PROPAV', blank=True, null=True)  # Field name made lowercase.
    appeal_a_currav = models.IntegerField(db_column='APPEAL_A_CURRAV', blank=True, null=True)  # Field name made lowercase.
    appeal_a_resltdate = models.TextField(db_column='APPEAL_A_RESLTDATE', blank=True, null=True)  # Field name made lowercase.
    is_selected = models.BooleanField(db_column='IS_SELECTED', default=False)

    class Meta:
        managed = True
        db_table = 'PropertyInfo'
