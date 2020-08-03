using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Serilog;
using Serilog.Events;
using System.Configuration;

namespace worker_service {
    public class Program {
        public static void Main (string[] args) {
            var _logFile = ConfigurationManager.AppSettings["LogFile"];
            Log.Logger = new LoggerConfiguration ()
                .MinimumLevel.Debug ()
                .MinimumLevel.Override ("Microsoft", LogEventLevel.Warning)
                .Enrich.FromLogContext ()
                .WriteTo.File (_logFile)
                .CreateLogger ();
            try {
                Log.Information ("Starting the service");
                CreateHostBuilder (args).Build ().Run ();
                return;
            } catch (Exception ex) {
                Log.Fatal (ex, "There was a problem starting the service");
                return;
            } finally {
                Log.CloseAndFlush ();
            }
        }

        public static IHostBuilder CreateHostBuilder (string[] args) {
            return Host.CreateDefaultBuilder (args)
                .UseWindowsService()
                .ConfigureServices ((hostContext, services) => {
                    services.AddHostedService<Worker> ();
                })
                .UseSerilog();
        }
    }
}