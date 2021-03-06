///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//	CAppPanel   version:  1.0   ? date: 08/20/2009
//  -------------------------------------------------------------
//  
//  -------------------------------------------------------------
//	Copyright (C) 2009 dasjack- All Rights Reserved
//	Written By Jack Liu
//	created:	14:9:2009   16:23
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#pragma once
#include "dpanel.h"
#include "slidebehavior.h"
#include <utility/stringfun.h>

#include <boost/algorithm/string.hpp>

HWND		_MainHwnd;
/**
*	parse the tstring options,return in a vector
*/
inline vector<CString> ParseCmdLine(LPCTSTR pcmdline,LPCTSTR filter=_T(" "))
{
	vector<CString> res_vec;
	//split tstring into vector
	vector<tstring> pws;
	boost::split(pws,pcmdline,boost::is_any_of(filter));

	for(size_t i=0;i<pws.size();i++)
	{
		if (pws[i].length())
		{
			res_vec.push_back(pws[i].c_str());
			//OutputDebugString(pws[i].c_str());
		}
	}
	return res_vec;
}
//////////////////////////////////////////////////////////////////////////
#define  FIRSTSUBID	5000
#define WM_SHOWPOPPANEL WM_USER+1210
/**
*
*/
BOOL HasFullScreenWindow()
{
	CWindow curWnd = GetForegroundWindow();

	return curWnd.IsWindow()?curWnd.IsZoomed():FALSE;
}
//
BOOL NeedShowPop=TRUE;
/**
*
*/
void CALLBACK OnPopTimerProc(HWND hwnd,UINT uMsg,UINT_PTR idEvent,DWORD dwTime)
{
	if(!HasFullScreenWindow() && NeedShowPop)
	{
		::PostMessage(_MainHwnd,WM_SHOWPOPPANEL,1,0);
	}
}
/************************************************************************
* 
*
*
/************************************************************************/
class CPopPanel : public CWebPanel
							,public CSlideBehavior<CPopPanel>
{
public:
	BEGIN_MSG_MAP_EX(CPopPanel)
		COMMAND_ID_HANDLER(IDOK, OnClose)
		MSG_WM_USERDEF(WM_SHOWPOPPANEL,OnShowPop)
		MSG_WM_USERDEF(WM_BROWSEREVENT,OnBrowserEvent)
		CHAIN_MSG_MAP(CWebPanel)
	END_MSG_MAP()
	/**
	*
	*/
	LRESULT OnClose(WORD /*wNotifyCode*/, WORD wID, HWND /*hWndCtl*/, BOOL& /*bHandled*/)
	{
		//g_isopen = FALSE;
		//CloseDialog(wID);
		ShowWindow(SW_HIDE); 
		return TRUE;
	}
	/**
	*
	*/
	void OnShowPop(WPARAM wParam,LPARAM lParam)
	{
		if(wParam)
		{
			Refresh();
			if(m_htimer)
			{
				KillTimer(m_htimer);
				m_htimer = 0;
			}
			NeedShowPop = FALSE;
		}
	}
public:
	/**
	*
	*/
	CPopPanel(LPCTSTR clsname,LPCTSTR cfgpath,const BOOL isheaped=FALSE):CWebPanel(clsname,cfgpath,isheaped)
		,m_htimer(0),m_pwidth(0),m_pheight(0)
	{
	}
	/**
	*
	*/
	virtual BOOL PreTranslateWebInvoke(CString& apiname,vector<CString>& params,CComVariant& res)
	{
		if (apiname == _T("app.quit"))
		{
			this->PostMessage(WM_COMMAND, IDOK, 0);
		}
		return FALSE;
	}
	virtual BOOL InitControls()
	{
		CWebPanel::InitControls();
		//CRect crect;
		//GetClientRect(&crect);
		ShowPopWindow();

		return TRUE;
	}
	void ShowPopWindow()
	{

		vector<CString> params=ParseCmdLine(m_cmdline);
		m_pwidth = 272;
		if(params.size()>0)
		{
			is_numeric(params[0],&m_pwidth);
		}
		m_pheight = 192;
		if(params.size()>1)
		{
			is_numeric<DWORD>(params[1],&m_pheight);
		}
		m_url = _T("http://gacenter.ztgame.com:8100/pop.html");
		if(params.size()>2)
		{
			m_url = params[2];
		}
		int   sx = GetSystemMetrics(SM_CXSCREEN);   
		int   sy= GetSystemMetrics(SM_CYSCREEN);
		//int x = GetConfigInt(m_cfgpath,_T("poppanel"),_T("x"),1);
		//int y = GetConfigInt(m_cfgpath,_T("poppanel"),_T("y"),40);
		MoveWindow(sx-m_pwidth-1, sy-m_pheight-40, m_pwidth, m_pheight);
		//SetWindowPos(HWND_TOPMOST, sx-m_pwidth-x, sy-m_pheight-y, m_pwidth, m_pheight,SWP_SHOWWINDOW);
		ModifyStyleEx(0,WS_EX_TOOLWINDOW,SWP_NOMOVE);


		NeedShowPop = TRUE;
		if(!m_htimer)
		{
			m_htimer=::SetTimer(NULL,9998,1000,OnPopTimerProc);
		}

	}
	/**
	*
	*/
	void OnBrowserEvent(WPARAM wParam,LPARAM lParam)
	{
		DWORD event_id = (DWORD)wParam;
		if (event_id == DISPID_NAVIGATEERROR )//network is not connected
		{
			m_webwnd.ShowWindow(SW_HIDE);
		}
		else if(event_id == DISPID_DOCUMENTCOMPLETE)
		{
			Slide(TRUE);
		}
		else if(wParam == DISPID_GetHostInfo)
		{
			CWebCtrlUIHandler::WB_GetHostInfo* pInfo = (CWebCtrlUIHandler::WB_GetHostInfo*)lParam;
			*(pInfo->pdwFlags) = DOCHOSTUIFLAG_NO3DBORDER \
				| DOCHOSTUIFLAG_SCROLL_NO \
				| DOCHOSTUIFLAG_THEME \
				| DOCHOSTUIFLAG_USE_WINDOWED_SELECTCONTROL 
				| DOCHOSTUIFLAG_DIALOG //does not enable selection of the text in the form
				;
			*(pInfo->pdwDoubleClick) = DOCHOSTUIDBLCLK_DEFAULT;

		}
		else if (wParam == DISPID_ShowContextMenu)
		{
			CWebCtrlUIHandler::WB_ShowContextMenu* pwbscm = (CWebCtrlUIHandler::WB_ShowContextMenu*)lParam;
			*(pwbscm->dwRetVal) = S_OK;
		}
		else
		{
			SetMsgHandled(FALSE);
		}
	}
	/**
	*
	*/
	void Refresh()
	{
		//main interface
		CString strUrl = m_url;
		strUrl +=_T("?id=")+GenDeviceID();
		Load(strUrl);
		::SetWindowPos(this->m_hWnd,HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE);

	}
public:
	/**
	*called when some msg coming
	*for simple ,just a notify ,no type,no param
	*/
public:
	CString m_cmdline;
protected:
	DWORD		m_pwidth;
	DWORD		m_pheight;
	CString		m_url;
	UINT_PTR	m_htimer;
};
