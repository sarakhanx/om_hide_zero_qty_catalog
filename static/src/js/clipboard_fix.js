odoo.define('om_hide_zero_qty_catalog.clipboard_fix', function (require) {
    'use strict';

    // Import the Dialog class - using the appropriate path for Odoo 17
    const { Component } = require("@odoo/owl");
    const { Dialog } = require("@web/core/dialog/dialog");
    const { _t } = require("web.core");
    
    // Try different ways to find the RPCErrorDialog component
    const webDialog = require("@web/core/errors/error_dialogs");
    const RPCErrorDialog = webDialog.RPCErrorDialog || false;
    
    // If we found the RPCErrorDialog component, patch it
    if (RPCErrorDialog) {
        const originalOnClickClipboard = RPCErrorDialog.prototype.onClickClipboard || 
                                        RPCErrorDialog.prototype._onClickClipboard;
        
        if (originalOnClickClipboard) {
            // Patch the click handler
            const patchedClickHandler = function (ev) {
                try {
                    // Check if clipboard API is available
                    if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
                        // Use the original function if clipboard API is available
                        return originalOnClickClipboard.apply(this, arguments);
                    } else {
                        // Get the error text from wherever it might be in the component
                        let errorText = '';
                        if (this.props && this.props.error) {
                            errorText = this.props.error.message || '';
                            if (this.props.error.data && this.props.error.data.debug) {
                                errorText += '\n\n' + this.props.error.data.debug;
                            }
                        } else if (this.message) {
                            errorText = this.message;
                            if (this.traceback) {
                                errorText += '\n\n' + this.traceback;
                            }
                        }
                        
                        // Show in a dialog for manual copy
                        const dialogProps = {
                            title: _t('Clipboard API Not Available'),
                            body: `
                                <p>${_t('Clipboard access is not available in your browser. Please copy the error text below manually:')}</p>
                                <textarea rows="10" style="width:100%;font-family:monospace;">${errorText}</textarea>
                            `,
                            size: 'medium',
                        };
                        
                        if (Dialog.confirm) {
                            Dialog.confirm(undefined, dialogProps);
                        } else {
                            new Dialog(this, dialogProps).open();
                        }
                    }
                } catch (err) {
                    console.error('Error handling clipboard operation:', err);
                    // Show a notification (implementation may vary based on Odoo version)
                    if (this.env && this.env.services && this.env.services.notification) {
                        this.env.services.notification.add(
                            _t('Cannot copy to clipboard. Please copy the error message manually.'), 
                            { type: 'warning' }
                        );
                    } else if (this.displayNotification) {
                        this.displayNotification({
                            type: 'warning',
                            title: _t('Clipboard Error'),
                            message: _t('Cannot copy to clipboard. Please copy the error message manually.')
                        });
                    }
                }
            };

            // Apply the patch in a way that works for either prototype-based or class-based components
            if (RPCErrorDialog.prototype) {
                const methodName = RPCErrorDialog.prototype.onClickClipboard ? 
                                'onClickClipboard' : '_onClickClipboard';
                RPCErrorDialog.prototype[methodName] = patchedClickHandler;
            }
        }
    }
}); 