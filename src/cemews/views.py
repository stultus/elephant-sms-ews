from django.views import generic
from reports.models import Siting,Informer


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class SitingPage(generic.TemplateView):
    template_name = "sitings.html"

    def get_context_data(self,**kwargs):
        context = super(SitingPage, self).get_context_data(**kwargs)
        temp_locations = [list(i) for i in list(Siting.objects.all().values_list('location','message'))]
        locations = []
        for i in temp_locations:
            loc = []
            loc.append(str(i[1]))
            loc.append(float(i[0].split(",")[0]))
            loc.append(float(i[0].split(",")[1]))
            locations.append(loc)
        context['locations'] =locations
        return context

class ReportPage(generic.TemplateView):
    template_name = "report_api.html"

    def get_context_data(self, **kwargs):
        context = super(ReportPage,self).get_context_data(**kwargs)
        phone = self.request.GET['mb'][-10:]
        print phone
        message = self.request.GET['ms']
        print message
        informer = Informer.objects.filter(phone=phone).first()
        if informer:
            #decide wheather grid system or cordinate system
            msg_list = message.split()
            if len(msg_list)>2:
                if msg_list[1]=='c':
                    siting = Siting()
                    siting.location = msg_list[2]
                    siting.informer = informer
                    if len(msg_list)>3:
                        siting.message = " ".join(msg_list[3:])
                    siting.save()
                    print "Info stored successfully"

        else:
            print "Unknown informer, discarding the message"
        return context
