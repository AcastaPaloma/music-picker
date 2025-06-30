"use client"

/// ========== User ========== //
import useUser from "@/lib/useUser";

/// ========== Firebase ========== //
import { getAuth, signOut } from "firebase/auth";
import { app } from "@/lib/firebase"

/// ========== Router ========== //
import { useRouter } from "next/navigation";


/// ========== UI ========== //
import { Calendar, ChevronUp, Home, Inbox, Search, Settings, User2 } from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/components/ui/sidebar"

import { Button } from "@/components/ui/button"
import { IconCloudX } from "@tabler/icons-react"


// Menu items.
const items = [
  {
    title: "Home",
    url: "#",
    icon: Home,
  },
  {
    title: "Find songs",
    url: "#",
    icon: Inbox,
  },
  {
    title: "My portfolio",
    url: "#",
    icon: Calendar,
  },
]

export function AppSidebar() {
  const auth = getAuth(app);

  const { user, loading } = useUser();
  if (!user) return null;

  const router = useRouter();

  const handleLogout = async () => {
    try {
      await signOut(auth);
      console.log("User signed out");
      router.push("/")

    } catch (error) {
      console.error("Sign out error", error);
    }
  };
  

  return (
    <Sidebar>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Application</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild>
                    <a href={item.url}>
                      <item.icon />
                      <span>{item.title}</span>
                    </a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter>
        <SidebarMenu>
          <SidebarMenuItem>
            <Button onClick={handleLogout} variant="outline" size="sm">
              <IconCloudX /> Log out
            </Button>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarFooter>
    </Sidebar>
  );
}