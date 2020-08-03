using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System.Net.Http;

namespace worker_service {
    public class Worker : BackgroundService {
        private readonly ILogger<Worker> _logger;
        private HttpClient client;

        public Worker (ILogger<Worker> logger) {
            _logger = logger;
        }

        public override Task StartAsync(CancellationToken cancellationToken) {
            client = new HttpClient();
            return base.StartAsync(cancellationToken);
        }

        public override Task StopAsync(CancellationToken cancellationToken){
            client.Dispose();
            _logger.LogInformation("The service has been stopped...");
            return base.StopAsync(cancellationToken);
        }

        protected override async Task ExecuteAsync (CancellationToken stoppingToken) {
            while (!stoppingToken.IsCancellationRequested) {
                var result = await client.GetAsync("https://puneetreddy.com");
                if(result.IsSuccessStatusCode) {
                    _logger.LogInformation("The website is up. Status code {StatusCode}", result.StatusCode);
                } else {
                    _logger.LogError("The website is down. Status code {StatusCode}", result.StatusCode);
                    // Send out an e-mail or a SMS or some sort of notification.
                }
                await Task.Delay (5 * 1000, stoppingToken);
            }
        }
    }
}