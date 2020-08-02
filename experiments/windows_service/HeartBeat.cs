using System;
using System.IO;
using System.Timers;

namespace windows_service {
    public class HeartBeat {
        private readonly Timer _timer;

        public HeartBeat () {
            _timer = new Timer (1000) { AutoReset = true };
            _timer.Elapsed += TimerElapsed;
        }

        private void TimerElapsed (object sender, ElapsedEventArgs e) {
            string[] lines = new string[] { DateTime.Now.ToString () };
            File.AppendAllLines (@"C:\Temp\Demos\Heartbeat.txt", lines);
        }

        public void Start () {
            _timer.Start ();
        }

        public void Stop () {
            _timer.Stop ();
        }
    }
}