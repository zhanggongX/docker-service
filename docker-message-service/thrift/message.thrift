namespace java tech.zg.docker
namespace py message.api

service MessageService{
    bool send(1:string mobile, 2:string message);

    bool sendEmail(1:string email, 2: string message);
}