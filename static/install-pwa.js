window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent the default install prompt
    e.preventDefault();

    // Store the event for later use
    const deferredPrompt = e;

    // Show your custom install button
    myInstallButton.addEventListener('click', () => {
        // Show the install prompt
        deferredPrompt.prompt();

        // Wait for the user to respond to the prompt
        deferredPrompt.userChoice
            .then((choiceResult) => {
                if (choiceResult.outcome === 'accepted') {
                    console.log('User accepted the install prompt');
                }
            });

        // Clean up the deferred prompt
        deferredPrompt = null;
    });
});
