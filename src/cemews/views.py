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
        temp_locations = [list(i) for i in list(Siting.objects.all().values_list('created_at','location','message'))]
        locations = []
        for i in temp_locations:
            loc = []
            loc.append(str(i[2]))
            loc.append(float(i[1].split(",")[0]))
            loc.append(float(i[1].split(",")[1]))
            loc.append(str(i[0].date().day)+"-"+str(i[0].date().month)+"-"+str(i[0].date().year) +":")
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
                    if not len(msg_list[2].split(','))==2 or not msg_list[2].split(',')[1]:
                        return context
                    siting.location = msg_list[2]
                    siting.informer = informer
                    if len(msg_list)>3:
                        siting.message = " ".join(msg_list[3:])
                    siting.save()
                    print "Info stored successfully"

        else:
            print "Unknown informer, discarding the message"
        return context
