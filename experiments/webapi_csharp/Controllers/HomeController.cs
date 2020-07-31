using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using webapi_csharp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using webapi_csharp.Filters;
using webapi_csharp.Utilities;
using Microsoft.Extensions.FileProviders;

namespace webapi_csharp.Controllers {
    public class HomeController : Controller {
        private readonly ILogger<HomeController> _logger;

        public HomeController (ILogger<HomeController> logger) {
            _logger = logger;
        }

        [DisableFormValueModelBinding]
        public IActionResult Index () {
            var uploadPath = "C:\\Users\\css112720\\Desktop\\sandbox\\experiments\\webapi_csharp\\Data\\";
            IFileProvider physicalProvider = new PhysicalFileProvider(uploadPath);
            IndexModel iModel = new IndexModel(physicalProvider);
            return View (iModel);
        }

        public IActionResult Privacy () {
            return View ();
        }

        public IActionResult Upload() {
            return View();
        }

        [ResponseCache (Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error () {
            return View (new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}