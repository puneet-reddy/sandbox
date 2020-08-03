## Service Deployment Steps
### Windows
0. You need the Microsoft.Extensions.Hosting.WindowsServices library to use UseWindowsService in the builder.
1. Open powershell in admin mode
2. run `sc.exe create <ServiceName> binpath= <Path to service.exe> start= auto`
3. Go to the services window and start the service.
4. That's it. Your service is running!
5. To Uninstall it. 
    1. Stop the service.
    2. `sc.exe delete <ServiceName>`
