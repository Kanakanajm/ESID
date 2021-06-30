import React from 'react';
import {Typography} from '@material-ui/core';
import {useTranslation} from 'react-i18next';

import {makeStyles} from '@material-ui/core';

const useStyles = makeStyles({
  historyTitle: {
    paddingTop: '20px',
  },
});

export default function ResearchBar(): JSX.Element {
  const classes = useStyles();
  const {t} = useTranslation();

  return <Typography className={classes.historyTitle}>{t('history.placeholder')}</Typography>;
}
