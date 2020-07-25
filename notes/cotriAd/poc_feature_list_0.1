cotriAd PoC Feature List:
1. Client side app
	Initial ping and register with server.
		This will include the display details which the client is connected to.
	Send heartbeat to the scheduler server.
	Retrieve schedule form scheduler server and sync local schedule. 
	Connect to CDN/File Server and retrieve the ads in the schedule.
	Display the ads as per the schedule.
	Send updates to scheduler server along with heartbeat to update the status of the scheduled ads. This includes information regarding any scheduled ads which are not found in the CDN/File Server as well as any other failure information.
	*Assumptions*
	Scheduler server provides CDN/File Server details along with schedules to the client.
	Ads are already loaded on the CDN/File Server before being scheduled. (Server side requirement)
	
2. Server side file handler
	Upload video file to CDN. 
		Broken uploads must be resumable.
	Provide a download api for the uploaded files (wrapper around CDN?)
		Broken downloads must be resumable.
	Delete/remove video from CDN.
	
3. Scheduler server
	Provide a 24/7/365 schedule for ads
		Availability of clients
		Client details - display, bandwidth, video capability, etc.
	Keep track of all client devices health
		Number of missed heartbeats (Surrogate for packet loss)
		Last successful schedule sync.
		Missed/ failed schedule events.
	Send a client specific schedule to a client that makes a request for it.
	Expose CRUD API for use by the scheduler UI.
	Have business logic which 
		a) avoids scheduling conflicts.
		b) allows scheduling only on devices suitable for the ad being scheduled.

4. Auth server - Ignored for the POC

4. Scheduler & file upload webapp
	User login (Dummy)
	Display currently scheduled Ads. 
	CRUD for ad videos.
	Modify schedule
	(Stretch goal) have an in-page ad viewer to review uploaded ads.
	
Miscellaneous/Undecided features:
	Roku should automatically connect to available open networks.
	Auto detection of display when connected.
	Display driver installation? 
	Pre-loaded demo ads
	Admin screen for roku remote initial setup