// SPDX-FileCopyrightText: 2024 German Aerospace Center (DLR)
// SPDX-License-Identifier: Apache-2.0

import {createRoot} from 'react-dom/client';
import React from 'react';

// import App from './App';
import './util/i18n';
import SecureApp from 'SecureApp';

const rootEl = document.getElementById('root');
if (rootEl) {
  const root = createRoot(rootEl);
  root.render(<SecureApp />);
}
