using System;
using System.IO;
using System.Configuration;

namespace folder_monitor
{
    class Program
    {
        static void Main(string[] args)
        {
            string watchPath = ConfigurationManager.AppSettings["demoPath"];
            FileSystemWatcher watcher = new FileSystemWatcher(watchPath);
            watcher.EnableRaisingEvents = true;
            watcher.IncludeSubdirectories = true;
            watcher.Renamed += RenamedHandler;
            watcher.Created += CreatedHandler;
            watcher.Deleted += DeletedHandler;
            watcher.Changed += ChangedHandler;
            Console.ReadLine(); // Just to make sure the console stays open
        }

        static void RenamedHandler(object source, FileSystemEventArgs e) {
            Console.WriteLine($"Named changed to {e.Name}");
            Console.WriteLine(e.ToString());
        }

        static void CreatedHandler(object source, FileSystemEventArgs e) {
            Console.WriteLine($"Created a new file named {e.Name}");
        }

        static void DeletedHandler(object source, FileSystemEventArgs e) {
            Console.WriteLine($"Deleted {e.Name}");
        }

        static void ChangedHandler(object source, FileSystemEventArgs e) {
            Console.WriteLine($"Changed file {e.Name} at {System.DateTime.UtcNow}");
        }
    }
}
