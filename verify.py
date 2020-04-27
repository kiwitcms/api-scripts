from django.contrib.auth.models import User

from tcms.bugs.models import *
from tcms.testcases.models import *
from tcms.testplans.models import *
from tcms.testruns.models import *



try:
    from django_tenants.utils import schema_context
    from tcms_tenants.models import Tenant

    print("Multi tenant instance")
    print("Users=", User.objects.count())
    print("Tenants=", Tenant.objects.count())

    for tenant in Tenant.objects.all():
        with schema_context(tenant.schema_name):
            print(tenant.schema_name, "TC=", TestCase.objects.count())
            print(tenant.schema_name, "TP=", TestPlan.objects.count())
            print(tenant.schema_name, "TR=", TestRun.objects.count())
            print(tenant.schema_name, "TE=", TestExecution.objects.count())
            print(tenant.schema_name, "BS=", Bug.objects.count())
            print(tenant.schema_name, "AU=", tenant.authorized_users.count())

except ImportError:
    print("Single tenant instance")
    print("Users=", User.objects.count())
    print("TC=", TestCase.objects.count())
    print("TP=", TestPlan.objects.count())
    print("TR=", TestRun.objects.count())
    print("TE=", TestExecution.objects.count())
    print("BS=", Bug.objects.count())
